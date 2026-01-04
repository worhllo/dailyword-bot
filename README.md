# 🏐 Daily Haikyuu Bot (每日排球少年机器人)

> 一个基于 GitHub Actions 的零成本 Telegram 机器人，每日定时推送《排球少年！！》高清壁纸与正能量语录。

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/你的GitHub用户名/仓库名称/daily.yml?label=Build)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 项目简介

这是一个完全自动化、**零成本**运行的 Telegram 机器人。它利用 **GitHub Actions** 的定时任务功能，每天自动从 **Wallhaven** 获取一张《排球少年！！》的高清壁纸，并从 **一言 (Hitokoto)** 获取一句随机的动漫/哲学语录，推送到你的 Telegram 频道或群组。

**无需购买服务器，无需维护，Fork 即用！**

### ✨ 功能亮点

- **📅 每日定时推送**：默认每天北京时间早上 8:00 推送（时间可自定义）。
- **🖼️ 高清壁纸源**：接入 Wallhaven API，获取高质量二次元壁纸（支持随机筛选）。
- **💬 每日语录**：随机附带一句动漫或文学金句，每天都有新感觉。
- **🚀 Serverless**：完全依赖 GitHub Actions 运行，无需 VPS。
- **🛡️ 稳定可靠**：使用官方 API 接口，无需处理复杂的反爬虫验证。

---

## 📸 效果预览

<!-- 建议把你刚才那张成功的手机截图放在这里，非常直观 -->
![Screenshot_2025-12-21-00-21-50-77_948cd9899890cbd5c2798760b2b95377](https://github.com/user-attachments/assets/7cd983e7-c06a-4634-9cb1-277572c89418)

---

## 🚀 快速部署 (如何拥有自己的机器人)

你不需要懂代码，只需要按照以下步骤操作即可。

### 1. Fork 本仓库
点击页面右上角的 **Fork** 按钮，将本项目复制到你自己的 GitHub 账号下。

### 2. 准备 Telegram 机器人
1. 在 Telegram 中搜索 `@BotFather`。
2. 发送 `/newbot` 创建新机器人，获取 **Token**。
3. 创建一个频道 (Channel) 或群组，将机器人拉入并设为**管理员**。
4. 获取你的 **Chat ID** (可以使用 `@getidsbot` 获取)。

### 3. 配置 GitHub Secrets
为了安全起见，不要将 Token 直接写在代码里。请在你的 GitHub 仓库中配置环境变量：

1. 进入仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
2. 点击 **New repository secret**，添加以下两个变量：

| Name | Value (填入你的值) | 说明 |
| :--- | :--- | :--- |
| `BOT_TOKEN` | `123456:ABC-Def...` | 从 BotFather 获取的 Token |
| `CHAT_ID` | `-100xxxxxxx` | 你的频道或群组 ID (频道ID通常以 -100 开头) |

### 4. 启用定时任务
1. 点击仓库上方的 **Actions** 标签。
2. 你可能会看到一个警告："Workflows aren't being run on this forked repository"，点击绿色的 **I understand my workflows, go ahead and enable them**。
3. 在左侧选择 **Daily Hinata Push**，手动点击 **Run workflow** 测试一次。
4. 测试成功后，机器人将在每天固定时间自动运行。

---

## ⚙️ 自定义配置

### 修改推送时间
打开 `.github/workflows/daily.yml` 文件，修改 `cron` 表达式：

```yaml
on:
  schedule:
    # 每天 UTC 时间 0:00 (北京时间 8:00)
    - cron: '0 0 * * *'
如果你想改成北京时间早上 9 点，将第一个 0 改为 1 即可。
```
### 修改图片搜索关键词
打开 `main.py` 文件，找到 `url` 变量：
```# q=haikyuu 表示搜索排球少年，你可以改成 q=hinata shoyo (只看日向翔阳)
url = "https://wallhaven.cc/api/v1/search?q=haikyuu&categories=010&purity=100&sorting=random"
```
## 🛠️ 技术栈
Python 3
GitHub Actions (CI/CD)
Requests (HTTP Library)
Telegram Bot API
Wallhaven API (Image Source)
Hitokoto API (Quote Source)
## 🤝 致谢
感谢以下服务提供的免费 API：

- [Wallhaven](https://wallhaven.cc) - 最好的二次元壁纸站
- [Hitokoto 一言](https://hitokoto.cn) - 感动人心的文字
- 
## 📄 License
本项目采用 MIT License 开源协议。
---

## 📅 历史归档 (History)

| 日期 | 每日语录 | 精彩壁纸 |
| :--- | :--- | :---: |
<!-- HISTORY_START -->
| 2026-01-04 | “就算风吹散了冰雪，想念也会留存下来。”<br>——《滑头鬼之孙》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3vd3k.jpg' height='150'> |

| 2026-01-03 | “任尘世繁华，唯有守护你的一切，才是我此生唯一的使命。”<br>——《次元战争·红龙》 | <img src='https://w.wallhaven.cc/full/md/wallhaven-mdmrok.png' height='150'> |

| 2026-01-02 | “用我的左手将你那个不可理喻的幻想粉碎掉！”<br>——《魔法禁书目录》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od2vy5.jpg' height='150'> |

| 2026-01-01 | “跌跌撞撞的成长，又美又疼才是本质。”<br>——《哥斯拉不说话》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxyyrg.jpg' height='150'> |

| 2025-12-31 | “我命令你，喜欢我！”<br>——《加油大魔王》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2025-12-30 | “一定没有问题的！”<br>——《魔卡少女樱》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2025-12-29 | “就算风吹散了冰雪，想念也会留存下来。”<br>——《滑头鬼之孙》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-28 | “打架这玩意，不就是为了守护什么东西吗？”<br>——《银魂》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2025-12-27 | “须知政权是由枪杆子中取得的。”<br>——《八七会议报告》 | <img src='https://w.wallhaven.cc/full/vg/wallhaven-vge7r8.jpg' height='150'> |

| 2025-12-26 | “人生于我，一场豪赌而已。”<br>——《赡养人类》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2025-12-25 | “学而不厌，诲人不倦。”<br>——《论语·述而》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-24 | “如果当初握住的不是硬币，而是勇者的手......”<br>——《中二病也要谈恋爱 恋！》 | <img src='https://w.wallhaven.cc/full/wy/wallhaven-wy33zx.jpg' height='150'> |

| 2025-12-23 | “最短的捷径就是绕远路。”<br>——《STEEL BALL RUN》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2dr.jpg' height='150'> |

| 2025-12-22 | “就算天塌下来变成一片废墟，他的脸色也不会有丝毫变化。”<br>——《人生的智慧》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrovl.png' height='150'> |

| 2025-12-21 | “不可结缘，徒留寂寞……”<br>——《夏目友人帐》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-20 | “师者，所以传道授业解惑也。”<br>——《师说》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2025-12-20 | “学而不厌，诲人不倦。”<br>——《论语·述而》 | <img src='https://w.wallhaven.cc/full/5d/wallhaven-5d85j9.png' height='150'> |

<!-- HISTORY_END -->
