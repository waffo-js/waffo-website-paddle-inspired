#!/usr/bin/env python3
"""
从已下载的网站中提取文案内容并转换为 Markdown
保留原始目录结构
"""

import argparse
import os
import re
from pathlib import Path
from typing import Optional, List

from bs4 import BeautifulSoup
import html2text


class ContentExtractor:
    def __init__(
        self,
        source_dir: str,
        output_dir: str,
        verbose: bool = False,
        include_links: bool = True,
        ignore_empty: bool = True
    ):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        self.include_links = include_links
        self.ignore_empty = ignore_empty

        # 配置 html2text
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = not include_links
        self.h2t.ignore_images = False
        self.h2t.ignore_emphasis = False
        self.h2t.body_width = 0  # 不自动换行
        self.h2t.unicode_snob = True
        self.h2t.skip_internal_links = False

        # 统计
        self.processed_files = 0
        self.skipped_files = 0
        self.total_files = 0

        # 创建输出目录
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def log(self, message: str, verbose_only: bool = False):
        """打印日志"""
        if verbose_only and not self.verbose:
            return
        print(message)

    def should_skip_tag(self, tag) -> bool:
        """判断是否应该跳过该标签"""
        skip_tags = {
            'script', 'style', 'nav', 'header', 'footer',
            'iframe', 'noscript'
        }

        if tag.name in skip_tags:
            return True

        # 跳过常见的导航和页脚 class
        skip_classes = [
            'nav', 'navbar', 'navigation', 'header', 'footer',
            'sidebar', 'menu', 'cookie', 'popup', 'modal'
        ]

        tag_classes = tag.get('class', [])
        if isinstance(tag_classes, list):
            for cls in tag_classes:
                if any(skip in cls.lower() for skip in skip_classes):
                    return True

        return False

    def clean_html(self, soup: BeautifulSoup) -> BeautifulSoup:
        """清理 HTML，移除不需要的元素"""
        # 移除脚本和样式
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'iframe', 'noscript']):
            tag.decompose()

        # 移除常见的导航和页脚元素
        for tag in soup.find_all(class_=re.compile(r'nav|header|footer|cookie|popup|modal|sidebar', re.I)):
            tag.decompose()

        # 移除隐藏元素
        for tag in soup.find_all(style=re.compile(r'display:\s*none|visibility:\s*hidden', re.I)):
            tag.decompose()

        return soup

    def extract_metadata(self, soup: BeautifulSoup, url_path: str) -> dict:
        """提取页面元数据"""
        metadata = {
            'title': '',
            'description': '',
            'url': url_path
        }

        # 提取标题
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.get_text(strip=True)

        # 提取描述
        meta_desc = soup.find('meta', attrs={'name': 'description'}) or \
                   soup.find('meta', attrs={'property': 'og:description'})
        if meta_desc:
            metadata['description'] = meta_desc.get('content', '')

        return metadata

    def extract_main_content(self, soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """尝试提取主要内容区域"""
        # 尝试查找主要内容容器
        main_selectors = [
            'main',
            'article',
            '[role="main"]',
            '.main-content',
            '.content',
            '#main',
            '#content'
        ]

        for selector in main_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                return main_content

        # 如果没找到，返回 body
        return soup.find('body') or soup

    def html_to_markdown(self, html_content: str) -> str:
        """将 HTML 转换为 Markdown"""
        try:
            markdown = self.h2t.handle(html_content)

            # 清理多余的空行（3 个以上空行压缩为 2 个）
            markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)

            # 移除首尾空白
            markdown = markdown.strip()

            return markdown
        except Exception as e:
            self.log(f"  ⚠ Markdown 转换失败: {e}")
            return ""

    def process_html_file(self, html_path: Path) -> bool:
        """处理单个 HTML 文件"""
        try:
            # 读取 HTML
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            # 解析 HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # 获取相对路径
            rel_path = html_path.relative_to(self.source_dir)

            # 提取元数据
            metadata = self.extract_metadata(soup, str(rel_path))

            # 清理 HTML
            soup = self.clean_html(soup)

            # 提取主要内容
            main_content = self.extract_main_content(soup)

            # 转换为 Markdown
            markdown = self.html_to_markdown(str(main_content))

            # 检查是否为空
            if self.ignore_empty and len(markdown.strip()) < 50:
                self.log(f"  ⊘ 跳过（内容太少）: {rel_path}", verbose_only=True)
                self.skipped_files += 1
                return False

            # 构建完整的 Markdown 内容
            full_markdown = self.build_full_markdown(metadata, markdown)

            # 确定输出路径
            output_path = self.output_dir / rel_path.with_suffix('.md')
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # 保存 Markdown
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_markdown)

            self.log(f"  ✓ {rel_path} -> {output_path.relative_to(self.output_dir)}", verbose_only=True)
            self.processed_files += 1
            return True

        except Exception as e:
            self.log(f"  ✗ 处理失败 {html_path}: {e}")
            self.skipped_files += 1
            return False

    def build_full_markdown(self, metadata: dict, content: str) -> str:
        """构建完整的 Markdown 文档（包含元数据）"""
        lines = []

        # 添加 YAML 前置元数据
        lines.append('---')
        if metadata['title']:
            lines.append(f"title: \"{metadata['title']}\"")
        if metadata['description']:
            lines.append(f"description: \"{metadata['description']}\"")
        lines.append(f"source: \"{metadata['url']}\"")
        lines.append('---')
        lines.append('')

        # 添加标题
        if metadata['title']:
            lines.append(f"# {metadata['title']}")
            lines.append('')

        # 添加内容
        lines.append(content)

        return '\n'.join(lines)

    def find_html_files(self) -> List[Path]:
        """查找所有 HTML 文件"""
        html_files = []

        for html_file in self.source_dir.rglob('*.html'):
            html_files.append(html_file)

        for htm_file in self.source_dir.rglob('*.htm'):
            html_files.append(htm_file)

        return sorted(html_files)

    def extract_all(self):
        """提取所有内容"""
        self.log(f"\n开始提取内容...")
        self.log(f"源目录: {self.source_dir}")
        self.log(f"输出目录: {self.output_dir}\n")

        # 查找所有 HTML 文件
        html_files = self.find_html_files()
        self.total_files = len(html_files)

        if self.total_files == 0:
            self.log(f"✗ 未找到 HTML 文件在 {self.source_dir}")
            return

        self.log(f"找到 {self.total_files} 个 HTML 文件\n")

        # 处理每个文件
        for i, html_file in enumerate(html_files, 1):
            self.log(f"[{i}/{self.total_files}] 处理: {html_file.relative_to(self.source_dir)}")
            self.process_html_file(html_file)

        # 生成索引
        self.generate_index()

        # 显示统计
        self.log(f"\n{'=' * 60}")
        self.log(f"✓ 提取完成！")
        self.log(f"  - 总文件数: {self.total_files}")
        self.log(f"  - 成功处理: {self.processed_files}")
        self.log(f"  - 跳过文件: {self.skipped_files}")
        self.log(f"  - 输出目录: {self.output_dir}")
        self.log(f"{'=' * 60}\n")

    def generate_index(self):
        """生成索引文件"""
        try:
            index_path = self.output_dir / 'INDEX.md'

            lines = [
                '# 内容索引',
                '',
                f'从 `{self.source_dir}` 提取的内容',
                '',
                '## 文件列表',
                ''
            ]

            # 收集所有生成的 markdown 文件
            md_files = sorted(self.output_dir.rglob('*.md'))
            md_files = [f for f in md_files if f.name != 'INDEX.md']

            # 按目录组织
            current_dir = None
            for md_file in md_files:
                rel_path = md_file.relative_to(self.output_dir)
                parent = rel_path.parent

                if parent != current_dir:
                    current_dir = parent
                    if str(parent) != '.':
                        lines.append(f'\n### {parent}/')
                        lines.append('')

                # 读取标题
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        title_match = re.search(r'^title:\s*"(.+)"', content, re.MULTILINE)
                        title = title_match.group(1) if title_match else md_file.stem
                except:
                    title = md_file.stem

                lines.append(f'- [{title}]({rel_path})')

            lines.append('')
            lines.append(f'\n---\n生成时间: {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))

            self.log(f"\n✓ 已生成索引: {index_path}", verbose_only=True)

        except Exception as e:
            self.log(f"⚠ 生成索引失败: {e}")


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='从 HTML 文件中提取内容并转换为 Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  %(prog)s paddle_clone/ paddle_content/

  # 详细输出
  %(prog)s paddle_clone/ paddle_content/ -v

  # 不包含链接
  %(prog)s paddle_clone/ paddle_content/ --no-links

  # 包含所有文件（即使内容很少）
  %(prog)s paddle_clone/ paddle_content/ --include-all
        """
    )

    parser.add_argument(
        'source',
        help='源目录（包含 HTML 文件）'
    )
    parser.add_argument(
        'output',
        help='输出目录（Markdown 文件）'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='详细输出'
    )
    parser.add_argument(
        '--no-links',
        action='store_true',
        help='不包含链接'
    )
    parser.add_argument(
        '--include-all',
        action='store_true',
        help='包含所有文件（不跳过内容少的文件）'
    )

    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()

    # 检查源目录
    if not os.path.exists(args.source):
        print(f"✗ 错误: 源目录不存在: {args.source}")
        return 1

    # 创建提取器
    extractor = ContentExtractor(
        source_dir=args.source,
        output_dir=args.output,
        verbose=args.verbose,
        include_links=not args.no_links,
        ignore_empty=not args.include_all
    )

    try:
        extractor.extract_all()
        return 0
    except KeyboardInterrupt:
        print("\n\n⚠ 用户中断")
        return 1
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
