import requests
import os
import random
import time
from datetime import datetime
import re

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. 伪装头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_daily_quote():
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    try:
        res = requests.get(api_url, headers=HEADERS, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"“{data.get('hitokoto')}”<br>——《{data.get('from')}》"
    except Exception:
        pass
    return "“排球是永远向上看的运动！”<br>——《排球少年！！》"

def get_haikyuu_image():
    url = "https://wallhaven.cc/api/v1/search?q=haikyuu&categories=010&purity=100&sorting=random"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            post_list = data.get('data', [])
            if post_list:
                post = random.choice(post_list)
                return post.get('path')
    except Exception as e:
        print(f"请求异常: {e}")
    return None

def update_readme(quote, img_url):
    """
    将内容写入 README.md
    """
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return

    # 获取今天的日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 构造 Markdown 表格行
    # 图片用 HTML 标签限制宽度，防止太占位置
    new_row = f"| {today} | {quote} | <img src='{img_url}' width='200'> |\n"

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 寻找定位标记
        marker = "<!-- HISTORY_START -->"
        if marker in content:
            # 在标记后面插入新的一行，这样最新的会在最上面
            new_content = content.replace(marker, marker + "\n" + new_row)
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("✅ README 更新成功！")
        else:
            print("⚠️ 未在 README 中找到定位标记 <!-- HISTORY_START -->")
            
    except Exception as e:
        print(f"❌ 更新 README 失败: {e}")

def send_telegram(img_url):
    # 注意：为了让 README 显示好看，我在 get_daily_quote 里把换行改成了 <br>
    # 但发给 Telegram 需要把 <br> 换回换行符
    quote_html = get_daily_quote()
    quote_text = quote_html.replace("<br>", "\n")
    
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = f"{quote_text}\n\n🏐 <b>每日排球少年</b>\n#Haikyuu #Wallhaven"

    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    
    try:
        print("正在推送给 Telegram...")
        res = requests.post(send_url, data=payload, timeout=20)
        print(f"Telegram 推送状态: {res.status_code}")
        
        if res.status_code == 200:
            # 只有发送成功了，才去写 README
            print("正在写入历史归档...")
            update_readme(quote_html, img_url)
            
    except Exception as e:
        print(f"发送异常: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("致命错误：Secrets 未配置！")
        exit(1)
    else:
        print("=== 任务开始 ===")
        pic = get_haikyuu_image()
        
        if pic:
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            exit(1)
