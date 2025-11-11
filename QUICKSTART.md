# 快速开始指南

## 5 分钟上手

### 1️⃣ 安装依赖

```bash
pip install requests beautifulsoup4 lxml
```

或使用 requirements.txt：

```bash
pip install -r requirements.txt
```

### 2️⃣ 基本使用

克隆任意网站：

```bash
python paddle_cloner.py https://example.com ./output
```

就这么简单！🎉

---

## 常见使用场景

### 📚 场景 1: 克隆文档站点

```bash
# 克隆一个技术文档网站
python paddle_cloner.py https://docs.python.org ./python-docs -d 4 -v
```

### 🎨 场景 2: 克隆营销网站（含外部资源）

```bash
# 包括 CDN 上的图片、字体等
python paddle_cloner.py https://mysite.com ./mysite-backup --allow-external
```

### 🔍 场景 3: 快速预览（浅层爬取）

```bash
# 只爬首页和直接链接的页面
python paddle_cloner.py https://example.com ./preview -d 1
```

### 🐌 场景 4: 礼貌爬取（慢速）

```bash
# 对服务器更友好
python paddle_cloner.py https://example.com ./output --delay 2.0
```

### ⚡ 场景 5: 开发调试（快速）

```bash
# 仅用于开发测试！
python paddle_cloner.py https://localhost:3000 ./local-copy \
  --skip-robots --delay 0.1 -v
```

---

## 参数速查表

| 我想... | 使用参数 |
|--------|---------|
| 爬取更多页面 | `-d 10` |
| 更快速度 | `--delay 0.1` |
| 更慢速度（礼貌） | `--delay 2.0` |
| 下载外部资源 | `--allow-external` |
| 查看详细日志 | `-v` |
| 跳过 robots.txt | `--skip-robots` |
| 增加超时时间 | `--timeout 120` |
| 自定义 UA | `--user-agent "MyBot"` |

---

## 查看帮助

```bash
python paddle_cloner.py -h
```

---

## 检查下载结果

下载完成后，可以直接在浏览器中打开：

```bash
# macOS
open ./output/index.html

# Linux
xdg-open ./output/index.html

# Windows
start ./output/index.html
```

或使用本地服务器：

```bash
# Python 3
cd output
python -m http.server 8000

# 然后访问 http://localhost:8000
```

---

## 故障排查速查

### ❌ 没有下载任何文件

1. 检查 robots.txt：`--skip-robots`
2. 增加深度：`-d 10`
3. 查看详细日志：`-v`

### ❌ 样式/图片丢失

1. 允许外部资源：`--allow-external`
2. 检查网站是否使用 JS 动态加载

### ❌ 请求超时

1. 增加超时：`--timeout 120`
2. 检查网络连接

### ❌ 被网站阻止

1. 更改 User-Agent：`--user-agent "Mozilla/5.0..."`
2. 增加延迟：`--delay 2.0`

---

## 下一步

- 📖 阅读完整的 [README.md](README.md)
- 💻 查看 [example_usage.py](example_usage.py) 了解如何在代码中使用
- 🔧 修改 `paddle_cloner.py` 以适应你的需求

---

## ⚠️ 重要提醒

- ✅ 仅用于学习和个人使用
- ✅ 遵守网站的服务条款
- ✅ 使用合理的延迟，不要对服务器造成负担
- ✅ 尊重版权和知识产权
- ❌ 不要用于商业目的（除非获得授权）
- ❌ 不要爬取需要登录的内容
- ❌ 不要用于恶意目的

---

Happy Cloning! 🚀
