# 静态网站克隆工具 (Static Site Cloner)

一个通用的 Python 爬虫工具，用于递归下载网站的所有静态资源（HTML、CSS、JS、图片、字体等）并保持原始目录结构。

## 功能特性

- ✅ 递归爬取网站页面和资源
- ✅ 保持原始目录结构
- ✅ 自动替换 URL 为本地相对路径
- ✅ 遵守 robots.txt（可选）
- ✅ 深度控制（避免过度爬取）
- ✅ 跳过 API 端点
- ✅ 详细的日志输出
- ✅ 可配置的请求延迟和超时
- ✅ 自定义 User-Agent
- ✅ 支持外部资源下载（可选）

## 安装依赖

```bash
pip install -r requirements.txt
```

## 基本用法

```bash
# 最简单的用法
python paddle_cloner.py https://example.com ./output

# 查看帮助
python paddle_cloner.py -h
```

## 命令行参数

### 必需参数

- `url` - 目标网站 URL（例如：https://example.com）
- `output` - 输出目录路径

### 可选参数

| 参数 | 简写 | 默认值 | 说明 |
|-----|------|--------|------|
| `--max-depth` | `-d` | 3 | 最大爬取深度 |
| `--delay` | - | 0.5 | 请求间延迟（秒） |
| `--timeout` | - | 30 | 请求超时时间（秒） |
| `--user-agent` | - | CloneBot/1.0... | 自定义 User-Agent |
| `--skip-robots` | - | False | 跳过 robots.txt 检查 |
| `--verbose` | `-v` | False | 详细输出模式 |
| `--allow-external` | - | False | 允许下载外部域名资源 |

## 使用示例

### 1. 基本克隆（使用默认设置）

```bash
python paddle_cloner.py https://paddle.com ./paddle_clone
```

### 2. 增加爬取深度

```bash
python paddle_cloner.py https://example.com ./output -d 5
```

### 3. 加快爬取速度（减少延迟）

```bash
python paddle_cloner.py https://example.com ./output --delay 0.1
```

### 4. 详细模式 + 跳过 robots.txt

```bash
python paddle_cloner.py https://example.com ./output -v --skip-robots
```

### 5. 下载包含外部 CDN 资源

```bash
python paddle_cloner.py https://example.com ./output --allow-external
```

### 6. 完整配置示例

```bash
python paddle_cloner.py https://example.com ./output \
  -d 5 \
  --delay 1.0 \
  --timeout 60 \
  --user-agent "MyBot/1.0" \
  --verbose \
  --allow-external
```

## 输出示例

```
开始爬取: https://paddle.com
输出目录: ./paddle_clone
最大深度: 3
请求延迟: 0.5秒
请求超时: 30秒

[深度 0] 正在处理: https://paddle.com
  [GET] https://paddle.com -> 200
  ✓ 保存到: paddle_clone/index.html

[深度 0] 正在处理: https://paddle.com/assets/style.css
  [GET] https://paddle.com/assets/style.css -> 200
  ✓ 保存到: paddle_clone/assets/style.css

[深度 1] 正在处理: https://paddle.com/pricing
  [GET] https://paddle.com/pricing -> 200
  ✓ 保存到: paddle_clone/pricing.html

=== 第二阶段：替换 URL 为本地路径 ===
  ✓ 已更新 HTML: paddle_clone/index.html
  ✓ 已更新 CSS: paddle_clone/assets/style.css

✓ 完成！共下载 156 个文件
✓ 文件保存在: ./paddle_clone
```

## 工作原理

1. **第一阶段：下载**
   - 使用广度优先搜索（BFS）遍历网站
   - 下载所有 HTML、CSS、JS、图片等资源
   - 保持原始目录结构
   - 遵守深度限制和 robots.txt

2. **第二阶段：URL 替换**
   - 遍历所有下载的 HTML 和 CSS 文件
   - 将绝对 URL 替换为相对路径
   - 确保本地浏览时链接正常工作

## 注意事项

### ⚠️ 法律和道德规范

- **尊重 robots.txt**：默认遵守网站的爬虫规则
- **控制速率**：使用适当的延迟（默认 0.5 秒），避免对服务器造成负担
- **遵守法律**：仅用于学习目的或已获授权的网站
- **版权尊重**：下载的内容可能受版权保护

### 🔧 技术限制

- **动态内容**：无法处理 JavaScript 动态生成的内容
- **需要登录**：无法爬取需要身份验证的页面
- **API 端点**：自动跳过 `/api/` 路径
- **外部资源**：默认不下载外部域名的资源（可通过 `--allow-external` 启用）

## 高级用法

### 自定义 User-Agent

某些网站可能会阻止默认的爬虫 User-Agent：

```bash
python paddle_cloner.py https://example.com ./output \
  --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

### 爬取深层页面

如果网站结构较深，可以增加深度限制：

```bash
python paddle_cloner.py https://example.com ./output -d 10
```

### 调试模式

使用详细模式查看所有操作细节：

```bash
python paddle_cloner.py https://example.com ./output -v
```

## 故障排查

### 问题：下载的文件数量很少

**可能原因：**
- robots.txt 阻止了爬取
- 深度限制太低
- 网站使用 JavaScript 动态加载内容

**解决方案：**
```bash
# 尝试跳过 robots.txt 和增加深度
python paddle_cloner.py https://example.com ./output --skip-robots -d 10
```

### 问题：链接无法正常工作

**可能原因：**
- 外部资源未下载
- 动态内容未被处理

**解决方案：**
```bash
# 允许下载外部资源
python paddle_cloner.py https://example.com ./output --allow-external
```

### 问题：请求超时

**可能原因：**
- 网络连接慢
- 服务器响应慢

**解决方案：**
```bash
# 增加超时时间
python paddle_cloner.py https://example.com ./output --timeout 120
```

## 依赖库

- `requests` - HTTP 请求库
- `beautifulsoup4` - HTML 解析库
- `lxml` - XML/HTML 解析器（可选，提升性能）

## 许可证

本工具仅供学习和研究目的使用。使用者需自行承担使用本工具的法律责任。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v2.0 (Generic Version)
- ✨ 支持命令行参数（URL、输出目录、深度等）
- ✨ 添加详细模式（`-v`）
- ✨ 可配置请求延迟和超时
- ✨ 支持外部资源下载（`--allow-external`）
- ✨ 可选跳过 robots.txt（`--skip-robots`）
- 🐛 改进日志输出系统

### v1.0 (Original)
- ✨ 基本爬取功能
- ✨ 遵守 robots.txt
- ✨ URL 替换为本地路径
