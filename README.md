# GG - GitHub 通知查看器 🎵

一个有趣的命令行工具，用于查看 GitHub 通知并提供音乐播放功能。

## ✨ 特性

- 🔔 **GitHub 通知查看**: 快速获取和查看未读的 GitHub 通知
- 🎵 **音乐播放**: 集成 pygame 音乐播放器，支持基本的播放控制
- 📝 **通知记录**: 自动将通知保存到本地文件
- 🎮 **交互式控制**: 音乐播放时支持暂停、继续、下一首等操作

## 🛠 安装

### 前置要求

- Python 2.7
- pygame (用于音乐播放功能)

### 安装步骤

1. 克隆项目:
```bash
git clone https://github.com/MrKiven/gg.git
cd gg
```

2. 安装依赖:
```bash
pip install -r requirements.txt
# 或直接安装
pip install requests==2.20.0 pygame
```

3. 安装 GG:
```bash
python setup.py install
```

## ⚙️ 配置

### GitHub Token 配置

1. 在项目根目录创建 `MrKiven.token` 文件
2. 将你的 GitHub Personal Access Token 写入该文件

获取 GitHub Token 的步骤：
1. 访问 [GitHub Settings > Personal access tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token"
3. 选择 `notifications` 权限
4. 生成并复制 token 到 `MrKiven.token` 文件

### 音乐文件配置

如需使用音乐播放功能，请修改 `gg/music.py` 中的 `_songs` 列表，添加你的音乐文件路径：

```python
_songs = [
    '/path/to/your/music1.mp3',
    '/path/to/your/music2.mp3'
]
```

## 🚀 使用方法

### 查看 GitHub 通知

```bash
shit
```

该命令会：
- 获取你的未读 GitHub 通知
- 在终端显示通知详情（包括仓库名称和标题）
- 将通知保存到 `notifications.txt` 文件

### 播放音乐

```bash
shit --music
```

音乐播放时支持以下命令：
- `start` - 继续播放（取消暂停）
- `stop` - 暂停播放
- `next` - 播放下一首
- `restart` - 重新开始当前歌曲
- `quit` - 退出播放器

### 其他选项

```bash
# 查看版本
shit --version

# 查看帮助
shit --help

# 指定通知ID（默认 -1）
shit -i 5
```

## 📁 项目结构

```
gg/
├── gg/
│   ├── __init__.py          # 版本信息
│   ├── consts.py           # 常量定义
│   ├── gg.py              # 主要功能实现
│   └── music.py           # 音乐播放功能
├── README.md              # 项目说明
└── setup.py              # 安装配置
```

## 📋 依赖项

- `requests==2.20.0` - 用于 GitHub API 调用
- `pygame` - 用于音乐播放功能
- `click` - 用于命令行界面

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📄 许可证

该项目仅供娱乐和学习使用。

## 👤 作者

**kiven**
- Email: kiven.mr@gmail.com
- GitHub: [@MrKiven](https://github.com/MrKiven)

---

*Just For Fun~~~~~~* 🎉

