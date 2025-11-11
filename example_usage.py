#!/usr/bin/env python3
"""
示例：如何在 Python 代码中使用 StaticSiteCloner
"""

from paddle_cloner import StaticSiteCloner


def example_1_basic():
    """示例 1: 基本用法"""
    print("=== 示例 1: 基本用法 ===\n")

    cloner = StaticSiteCloner(
        base_url='https://example.com',
        output_dir='./example_output'
    )

    try:
        cloner.crawl()
    except KeyboardInterrupt:
        print("\n用户中断")


def example_2_custom_settings():
    """示例 2: 自定义设置"""
    print("=== 示例 2: 自定义设置 ===\n")

    cloner = StaticSiteCloner(
        base_url='https://example.com',
        output_dir='./custom_output',
        max_depth=5,                    # 增加深度
        delay=1.0,                      # 更慢的请求（更礼貌）
        user_agent='MyBot/2.0',         # 自定义 User-Agent
        skip_robots=False,              # 遵守 robots.txt
        verbose=True,                   # 详细输出
        timeout=60,                     # 60 秒超时
        skip_external=True              # 只下载同域名资源
    )

    try:
        cloner.crawl()
    except KeyboardInterrupt:
        print("\n用户中断")


def example_3_allow_external():
    """示例 3: 允许外部资源（包括 CDN）"""
    print("=== 示例 3: 允许外部资源 ===\n")

    cloner = StaticSiteCloner(
        base_url='https://example.com',
        output_dir='./with_external',
        skip_external=False,            # 下载外部资源
        verbose=True
    )

    try:
        cloner.crawl()
    except KeyboardInterrupt:
        print("\n用户中断")


def example_4_fast_crawl():
    """示例 4: 快速爬取（不推荐用于生产环境）"""
    print("=== 示例 4: 快速爬取 ===\n")

    cloner = StaticSiteCloner(
        base_url='https://example.com',
        output_dir='./fast_output',
        max_depth=2,                    # 较浅的深度
        delay=0.1,                      # 很短的延迟（请谨慎使用！）
        skip_robots=True,               # 跳过 robots.txt（请谨慎使用！）
        timeout=15,                     # 较短的超时
        verbose=False                   # 简洁输出
    )

    try:
        cloner.crawl()
    except KeyboardInterrupt:
        print("\n用户中断")


def example_5_with_error_handling():
    """示例 5: 完整的错误处理"""
    print("=== 示例 5: 完整错误处理 ===\n")

    try:
        cloner = StaticSiteCloner(
            base_url='https://example.com',
            output_dir='./error_handling_output',
            verbose=True
        )

        cloner.crawl()

        # 访问下载统计
        print(f"\n下载完成：")
        print(f"  - 总文件数: {len(cloner.downloaded_files)}")
        print(f"  - 访问的 URL: {len(cloner.visited_urls)}")
        print(f"  - 输出目录: {cloner.output_dir}")

    except KeyboardInterrupt:
        print("\n⚠ 用户中断爬取")
        print(f"已下载 {len(cloner.downloaded_files)} 个文件")

    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        import traceback
        traceback.print_exc()


def example_6_multiple_sites():
    """示例 6: 批量下载多个网站"""
    print("=== 示例 6: 批量下载 ===\n")

    sites = [
        ('https://example.com', './batch/example'),
        ('https://another-site.com', './batch/another'),
        ('https://third-site.com', './batch/third'),
    ]

    for url, output_dir in sites:
        print(f"\n{'=' * 60}")
        print(f"正在克隆: {url}")
        print(f"{'=' * 60}\n")

        try:
            cloner = StaticSiteCloner(
                base_url=url,
                output_dir=output_dir,
                max_depth=2,
                delay=1.0,
                verbose=False
            )

            cloner.crawl()

        except Exception as e:
            print(f"✗ 克隆 {url} 失败: {e}")
            continue

    print("\n✓ 所有网站克隆完成！")


if __name__ == '__main__':
    # 取消注释你想运行的示例：

    # example_1_basic()
    # example_2_custom_settings()
    # example_3_allow_external()
    # example_4_fast_crawl()
    example_5_with_error_handling()
    # example_6_multiple_sites()
