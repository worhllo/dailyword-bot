import requests
import os
import random

# 从 GitHub Secrets 获取配置
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def get_hinata_image():
    # Safebooru API 接口
    # tags=hinata_shouyou 表示搜索日向翔阳
    # rating:general 表示只要全年龄图片
    # json=1 表示返回 JSON 数据
    url = "https://safebooru.donmai.us/posts.json?tags=hinata_shouyou+rating:general&limit=20"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            if posts:
                # 随机选一张图
                selected_post = random.choice(posts)
                image_url = selected_post.get('file_url')
                return image_url
    except Exception as e:
        print(f"获取图片出错: {e}")
    return None

def send_telegram_photo(img_url):
    if not img_url:
        print("没有找到图片链接，跳过推送")
        return

    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": "🏐 每日日向翔阳！\n#Haikyuu #HinataShoyo"
    }
    
    try:
        res = requests.post(send_url, data=payload)
        print(f"推送状态: {res.status_code}")
        print(res.text)
    except Exception as e:
        print(f"发送消息出错: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("错误：请在 GitHub Secrets 中设置 BOT_TOKEN 和 CHAT_ID")
    else:
        print("开始寻找日向翔阳的图片...")
        pic = get_hinata_image()
        print(f"找到图片: {pic}")
        send_telegram_photo(pic)
