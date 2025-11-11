# 项目总览

## 📁 文件结构

```
paddle.com/
├── paddle_cloner.py       # 主脚本（通用版本）
├── example_usage.py       # Python 代码使用示例
├── requirements.txt       # Python 依赖
├── README.md             # 完整文档
├── QUICKSTART.md         # 快速开始指南
├── PROJECT_OVERVIEW.md   # 本文件
└── .gitignore           # Git 忽略规则
```

## 📄 文件说明

### `paddle_cloner.py`（主脚本）

**核心功能类：`StaticSiteCloner`**

主要方法：
- `__init__()` - 初始化配置
- `crawl()` - 开始爬取流程
- `download_file()` - 下载单个文件
- `process_html()` - 处理 HTML 文件，提取链接
- `process_css()` - 处理 CSS 文件，提取资源
- `replace_all_urls()` - 替换 URL 为本地路径

**命令行接口：**
- `parse_args()` - 解析命令行参数
- `main()` - 主入口函数

### `requirements.txt`（依赖列表）

```
requests>=2.31.0        # HTTP 请求
beautifulsoup4>=4.12.0  # HTML 解析
lxml>=4.9.0            # 解析器后端（性能优化）
```

### `example_usage.py`（使用示例）

包含 6 个示例场景：
1. 基本用法
2. 自定义设置
3. 允许外部资源
4. 快速爬取
5. 完整错误处理
6. 批量下载多个网站

### `README.md`（完整文档）

包含：
- 功能特性列表
- 安装说明
- 详细参数说明
- 使用示例
- 工作原理
- 注意事项
- 故障排查

### `QUICKSTART.md`（快速指南）

- 5 分钟快速上手
- 常见场景示例
- 参数速查表
- 故障排查速查

### `.gitignore`

防止以下内容被提交：
- 下载的网站内容
- Python 缓存
- 虚拟环境
- IDE 配置文件

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行脚本
```bash
# 方式 1: 命令行
python paddle_cloner.py https://example.com ./output

# 方式 2: Python 代码
python example_usage.py
```

## 🔧 核心技术

### 架构设计

```
用户输入
   ↓
命令行参数解析 (argparse)
   ↓
StaticSiteCloner 初始化
   ↓
第一阶段：下载
   ├─ BFS 广度优先遍历
   ├─ robots.txt 检查
   ├─ 同域名过滤
   ├─ API 端点跳过
   └─ 文件保存
   ↓
第二阶段：URL 替换
   ├─ 遍历 HTML 文件
   ├─ 遍历 CSS 文件
   └─ 替换为相对路径
   ↓
完成
```

### 关键算法

**1. BFS 爬取（广度优先搜索）**
```python
queue = [(base_url, 0)]
while queue:
    url, depth = queue.popleft()
    # 下载并处理
    # 提取链接并加入队列
```

**2. URL 标准化**
```python
# 移除 fragment (#section)
# 转换为绝对 URL
# 判断是否同域名
```

**3. 路径映射**
```python
URL: https://example.com/path/to/page
  ↓
本地: ./output/path/to/page.html
```

**4. URL 替换算法**
```python
# HTML: 使用 BeautifulSoup 解析和修改
# CSS: 使用正则表达式匹配 url(...)
# 计算相对路径
```

## 📊 性能考虑

### 时间复杂度
- 爬取：O(n) - n 为 URL 数量
- URL 替换：O(m) - m 为文件数量

### 空间复杂度
- 内存：O(n) - 存储已访问 URL 和下载映射
- 磁盘：取决于网站大小

### 优化建议

1. **并发下载**（未实现）
   - 可使用 `asyncio` + `aiohttp`
   - 预计性能提升 5-10 倍

2. **增量更新**（未实现）
   - 检查文件修改时间
   - 只下载变更内容

3. **压缩存储**（未实现）
   - 使用 gzip 压缩 HTML/CSS/JS
   - 减少磁盘占用 60-70%

## 🔍 代码统计

```
文件: paddle_cloner.py
├─ 行数: ~490 行
├─ 类: 1 个 (StaticSiteCloner)
├─ 方法: 15+ 个
└─ 函数: 2 个 (parse_args, main)
```

## 🎯 使用场景

### ✅ 适合
- 静态网站备份
- 离线浏览
- 网站迁移
- 学习 HTML 结构
- 文档归档

### ❌ 不适合
- SPA（单页应用）
- 需要登录的内容
- 动态加载的内容（AJAX）
- 需要 JavaScript 执行的页面
- 大型商业网站（法律风险）

## 📈 扩展性

### 可能的增强功能

1. **JavaScript 支持**
   - 集成 Selenium/Playwright
   - 处理动态内容

2. **登录支持**
   - Cookie 管理
   - Session 保持

3. **断点续传**
   - 保存进度
   - 恢复下载

4. **去重优化**
   - 内容哈希
   - 避免重复下载

5. **数据库存储**
   - 使用 SQLite
   - 更好的查询和管理

6. **GUI 界面**
   - 使用 Tkinter/PyQt
   - 可视化配置和进度

7. **Web 界面**
   - Flask/FastAPI 后端
   - 在线爬取服务

## 🛠️ 开发指南

### 添加新功能

1. 在 `StaticSiteCloner` 类中添加方法
2. 更新 `__init__` 参数（如需要）
3. 在 `parse_args()` 中添加命令行参数
4. 更新文档（README.md）
5. 添加示例（example_usage.py）

### 测试建议

```bash
# 使用本地测试服务器
python -m http.server 8000

# 然后爬取
python paddle_cloner.py http://localhost:8000 ./test
```

## 📝 版本历史

### v2.0 - 通用版本（当前）
- ✨ 完全通用，支持任意 URL
- ✨ 丰富的命令行参数
- ✨ 详细/简洁模式切换
- ✨ 外部资源控制
- 📚 完整的文档

### v1.0 - 原始版本
- ✨ 针对 paddle.com 的硬编码版本
- ✨ 基本爬取功能
- ✨ URL 替换

## 🤝 贡献指南

欢迎贡献！可以：
- 报告 Bug
- 建议新功能
- 提交 Pull Request
- 改进文档

## 📞 支持

遇到问题？
1. 查看 [README.md](README.md)
2. 查看 [QUICKSTART.md](QUICKSTART.md)
3. 运行 `python paddle_cloner.py -h`
4. 查看 [example_usage.py](example_usage.py)

## 📜 许可证

本项目仅供学习和研究使用。

---

最后更新：2025-11-11
