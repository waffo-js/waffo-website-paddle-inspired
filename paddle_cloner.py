#!/usr/bin/env python3
"""
Generic Static Site Cloner
递归下载网站的所有静态资源并保持目录结构
"""

import argparse
import os
import re
import sys
import time
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.robotparser import RobotFileParser
from pathlib import Path
from typing import Set, Dict, Optional
from collections import deque

import requests
from bs4 import BeautifulSoup


class StaticSiteCloner:
    def __init__(
        self,
        base_url: str,
        output_dir: str,
        max_depth: int = 3,
        delay: float = 0.5,
        user_agent: str = 'CloneBot/1.0 (For learning purposes only)',
        skip_robots: bool = False,
        verbose: bool = False,
        timeout: int = 30,
        skip_external: bool = True
    ):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.output_dir = Path(output_dir)
        self.max_depth = max_depth
        self.delay = delay
        self.skip_robots = skip_robots
        self.verbose = verbose
        self.timeout = timeout
        self.skip_external = skip_external

        # 追踪已访问的 URL
        self.visited_urls: Set[str] = set()
        self.downloaded_files: Dict[str, str] = {}  # URL -> 本地路径

        # 队列：(url, depth)
        self.queue = deque([(self.base_url, 0)])

        # 配置
        self.headers = {
            'User-Agent': user_agent
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # robots.txt 解析器
        self.robots = RobotFileParser()
        if not skip_robots:
            self.robots.set_url(urljoin(self.base_url, '/robots.txt'))
            try:
                self.robots.read()
                self.log(f"✓ 已读取 robots.txt", verbose=True)
            except Exception as e:
                self.log(f"⚠ 无法读取 robots.txt: {e}", verbose=True)

        # 创建输出目录
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def log(self, message: str, verbose: bool = False):
        """打印日志（支持详细模式）"""
        if verbose and not self.verbose:
            return
        print(message)

    def is_same_domain(self, url: str) -> bool:
        """检查 URL 是否属于同一域名"""
        return urlparse(url).netloc == self.domain

    def is_allowed(self, url: str) -> bool:
        """检查 robots.txt 是否允许访问"""
        if self.skip_robots:
            return True
        try:
            return self.robots.can_fetch(self.headers['User-Agent'], url)
        except:
            return True

    def is_api_endpoint(self, url: str) -> bool:
        """检查是否为 API 端点"""
        path = urlparse(url).path
        return '/api/' in path or path.startswith('/api')

    def normalize_url(self, url: str) -> str:
        """标准化 URL（移除 fragment）"""
        parsed = urlparse(url)
        return urlunparse(parsed._replace(fragment=''))

    def get_local_path(self, url: str) -> Path:
        """将 URL 转换为本地文件路径"""
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')

        # 如果是根路径或目录，添加 index.html
        if not path or path.endswith('/'):
            path = os.path.join(path, 'index.html')

        # 如果没有扩展名且不是资源文件，假定为 HTML
        if not os.path.splitext(path)[1]:
            path = path.rstrip('/') + '.html'

        return self.output_dir / path

    def download_file(self, url: str) -> Optional[bytes]:
        """下载文件内容"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            self.log(f"  [GET] {url} -> {response.status_code}")

            if response.status_code == 200:
                return response.content
            else:
                self.log(f"  ⚠ 状态码: {response.status_code}")
                return None

        except Exception as e:
            self.log(f"  ✗ 下载失败: {e}")
            return None

    def save_file(self, content: bytes, local_path: Path):
        """保存文件到本地"""
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(content)
        self.log(f"  ✓ 保存到: {local_path}", verbose=True)

    def extract_resources_from_html(self, soup: BeautifulSoup, current_url: str) -> Set[str]:
        """从 HTML 中提取所有资源链接"""
        resources = set()

        # 提取各种资源标签
        selectors = [
            ('link', 'href'),      # CSS, favicon, etc.
            ('script', 'src'),     # JavaScript
            ('img', 'src'),        # 图片
            ('img', 'srcset'),     # 响应式图片
            ('source', 'src'),     # 视频/音频源
            ('source', 'srcset'),  # 响应式图片源
            ('a', 'href'),         # 链接（HTML 页面）
        ]

        for tag_name, attr in selectors:
            for tag in soup.find_all(tag_name):
                value = tag.get(attr)
                if not value:
                    continue

                # 处理 srcset（多个 URL）
                if attr == 'srcset':
                    urls = [url.strip().split()[0] for url in value.split(',')]
                    for url in urls:
                        abs_url = urljoin(current_url, url)
                        resources.add(abs_url)
                else:
                    abs_url = urljoin(current_url, value)
                    resources.add(abs_url)

        return resources

    def extract_resources_from_css(self, css_content: str, current_url: str) -> Set[str]:
        """从 CSS 中提取资源链接（url(...)）"""
        resources = set()

        # 匹配 url(...) 模式
        pattern = r'url\([\'"]?([^\'")\s]+)[\'"]?\)'
        matches = re.findall(pattern, css_content)

        for match in matches:
            abs_url = urljoin(current_url, match)
            resources.add(abs_url)

        return resources

    def replace_urls_in_html(self, soup: BeautifulSoup, current_url: str) -> BeautifulSoup:
        """替换 HTML 中的 URL 为本地路径"""
        current_local_path = self.get_local_path(current_url)

        replacements = [
            ('link', 'href'),
            ('script', 'src'),
            ('img', 'src'),
            ('a', 'href'),
        ]

        for tag_name, attr in replacements:
            for tag in soup.find_all(tag_name):
                url = tag.get(attr)
                if not url:
                    continue

                abs_url = self.normalize_url(urljoin(current_url, url))

                # 如果已下载，替换为相对路径
                if abs_url in self.downloaded_files:
                    target_local_path = Path(self.downloaded_files[abs_url])
                    try:
                        rel_path = os.path.relpath(target_local_path, current_local_path.parent)
                        tag[attr] = rel_path
                    except:
                        pass

        return soup

    def replace_urls_in_css(self, css_content: str, current_url: str) -> str:
        """替换 CSS 中的 URL 为本地路径"""
        current_local_path = self.get_local_path(current_url)

        def replace_match(match):
            url = match.group(1)
            abs_url = self.normalize_url(urljoin(current_url, url))

            if abs_url in self.downloaded_files:
                target_local_path = Path(self.downloaded_files[abs_url])
                try:
                    rel_path = os.path.relpath(target_local_path, current_local_path.parent)
                    return f'url({rel_path})'
                except:
                    return match.group(0)
            return match.group(0)

        pattern = r'url\([\'"]?([^\'")\s]+)[\'"]?\)'
        return re.sub(pattern, replace_match, css_content)

    def process_html(self, url: str, content: bytes, depth: int):
        """处理 HTML 文件"""
        soup = BeautifulSoup(content, 'html.parser')

        # 提取所有资源
        resources = self.extract_resources_from_html(soup, url)

        # 将资源加入队列
        for resource_url in resources:
            resource_url = self.normalize_url(resource_url)

            if resource_url in self.visited_urls:
                continue

            if self.skip_external and not self.is_same_domain(resource_url):
                continue

            if self.is_api_endpoint(resource_url):
                self.log(f"  ⊘ 跳过 API: {resource_url}", verbose=True)
                continue

            # HTML 页面遵守深度限制，资源文件不限制
            parsed = urlparse(resource_url)
            is_html = (
                parsed.path.endswith('.html') or
                parsed.path.endswith('/') or
                not os.path.splitext(parsed.path)[1]
            )

            if is_html and depth + 1 > self.max_depth:
                continue

            # 加入队列
            new_depth = depth + 1 if is_html else depth
            self.queue.append((resource_url, new_depth))

    def process_css(self, url: str, content: bytes):
        """处理 CSS 文件"""
        css_text = content.decode('utf-8', errors='ignore')

        # 提取 CSS 中的资源
        resources = self.extract_resources_from_css(css_text, url)

        # 将资源加入队列（深度不增加）
        for resource_url in resources:
            resource_url = self.normalize_url(resource_url)

            if resource_url in self.visited_urls:
                continue

            if not self.is_same_domain(resource_url):
                continue

            self.queue.append((resource_url, 0))  # CSS 资源不计入深度

    def crawl(self):
        """开始爬取"""
        self.log(f"\n开始爬取: {self.base_url}")
        self.log(f"输出目录: {self.output_dir}")
        self.log(f"最大深度: {self.max_depth}")
        self.log(f"请求延迟: {self.delay}秒")
        self.log(f"请求超时: {self.timeout}秒\n")

        while self.queue:
            url, depth = self.queue.popleft()
            url = self.normalize_url(url)

            # 检查是否已访问
            if url in self.visited_urls:
                continue

            # 标记为已访问
            self.visited_urls.add(url)

            # 检查 robots.txt
            if not self.is_allowed(url):
                self.log(f"⊘ robots.txt 禁止: {url}", verbose=True)
                continue

            # 检查是否为 API 端点
            if self.is_api_endpoint(url):
                self.log(f"⊘ 跳过 API: {url}", verbose=True)
                continue

            # 显示进度
            self.log(f"\n[深度 {depth}] 正在处理: {url}")

            # 下载文件
            content = self.download_file(url)
            if not content:
                continue

            # 保存文件
            local_path = self.get_local_path(url)
            self.downloaded_files[url] = str(local_path)
            self.save_file(content, local_path)

            # 根据文件类型处理
            if url.endswith('.css') or 'text/css' in self.session.head(url).headers.get('content-type', ''):
                self.process_css(url, content)
            elif url.endswith(('.html', '.htm')) or 'text/html' in self.session.head(url).headers.get('content-type', ''):
                self.process_html(url, content, depth)

            # 礼貌延迟
            time.sleep(self.delay)

        # 第二遍：替换所有 URL
        self.log("\n\n=== 第二阶段：替换 URL 为本地路径 ===\n")
        self.replace_all_urls()

        self.log(f"\n✓ 完成！共下载 {len(self.downloaded_files)} 个文件")
        self.log(f"✓ 文件保存在: {self.output_dir}\n")

    def replace_all_urls(self):
        """第二遍遍历，替换所有文件中的 URL"""
        for url, local_path_str in self.downloaded_files.items():
            local_path = Path(local_path_str)

            if not local_path.exists():
                continue

            try:
                content = local_path.read_bytes()

                # HTML 文件
                if local_path.suffix in ['.html', '.htm']:
                    soup = BeautifulSoup(content, 'html.parser')
                    soup = self.replace_urls_in_html(soup, url)
                    local_path.write_text(str(soup), encoding='utf-8')
                    self.log(f"  ✓ 已更新 HTML: {local_path}", verbose=True)

                # CSS 文件
                elif local_path.suffix == '.css':
                    css_text = content.decode('utf-8', errors='ignore')
                    updated_css = self.replace_urls_in_css(css_text, url)
                    local_path.write_text(updated_css, encoding='utf-8')
                    self.log(f"  ✓ 已更新 CSS: {local_path}", verbose=True)

            except Exception as e:
                self.log(f"  ⚠ 无法更新 {local_path}: {e}")


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='递归下载网站的所有静态资源并保持目录结构',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  %(prog)s https://example.com ./output

  # 自定义深度和延迟
  %(prog)s https://example.com ./output -d 5 --delay 1.0

  # 详细模式 + 跳过 robots.txt
  %(prog)s https://example.com ./output -v --skip-robots

  # 允许外部资源
  %(prog)s https://example.com ./output --allow-external
        """
    )

    # 必需参数
    parser.add_argument(
        'url',
        help='目标网站 URL (例如: https://example.com)'
    )
    parser.add_argument(
        'output',
        help='输出目录路径'
    )

    # 可选参数
    parser.add_argument(
        '-d', '--max-depth',
        type=int,
        default=3,
        help='最大爬取深度 (默认: 3)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=0.5,
        help='请求间延迟秒数 (默认: 0.5)'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=30,
        help='请求超时秒数 (默认: 30)'
    )
    parser.add_argument(
        '--user-agent',
        default='CloneBot/1.0 (For learning purposes only)',
        help='自定义 User-Agent 字符串'
    )
    parser.add_argument(
        '--skip-robots',
        action='store_true',
        help='跳过 robots.txt 检查'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='详细输出模式'
    )
    parser.add_argument(
        '--allow-external',
        action='store_true',
        help='允许下载外部域名的资源（默认只下载同域名）'
    )

    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()

    # 验证 URL
    if not args.url.startswith(('http://', 'https://')):
        print(f"✗ 错误: URL 必须以 http:// 或 https:// 开头")
        sys.exit(1)

    # 创建爬虫实例
    cloner = StaticSiteCloner(
        base_url=args.url,
        output_dir=args.output,
        max_depth=args.max_depth,
        delay=args.delay,
        user_agent=args.user_agent,
        skip_robots=args.skip_robots,
        verbose=args.verbose,
        timeout=args.timeout,
        skip_external=not args.allow_external
    )

    try:
        cloner.crawl()
    except KeyboardInterrupt:
        print("\n\n⚠ 用户中断")
        print(f"已下载 {len(cloner.downloaded_files)} 个文件")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
