import requests
import os
import random
import time

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. 伪装浏览器头 (这是防止被拦截的关键！)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_daily_quote():
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    try:
        res = requests.get(api_url, headers=HEADERS, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"“{data.get('hitokoto')}”\n——《{data.get('from')}》"
    except Exception as e:
        print(f"[警告] 获取语录失败: {e}")
    return "“因为想赢，所以才会战斗！”\n——《排球少年！！》"

def get_hinata_image():
    # === 关键改动：将 safebooru.donmai.us 替换为 danbooru.donmai.us ===
    # Danbooru 拥有更庞大的图片库，且通常对 API 访问更宽松。
    # tags=hinata_shouyou+pixiv+rating:general 确保搜索日向翔阳、来自Pixiv、全年龄图片。
    url = "https://danbooru.donmai.us/posts.json?tags=hinata_shouyou+pixiv+rating:general&limit=20"
    
    print(f"正在请求 Danbooru 图库: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        print(f"Danbooru 图库响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            if posts:
                post = random.choice(posts)
                img_url = post.get('file_url') or post.get('sample_url')
                print(f"成功获取图片链接: {img_url}")
                return img_url
            else:
                print("错误：Danbooru 搜索结果为空 (可能标签太严格或图库暂时没数据)")
        else:
            print(f"错误：Danbooru 拒绝访问 (Status {response.status_code})")
            print(f"响应内容: {response.text[:100]}") # 打印前100个字符看看
            
    except Exception as e:
        print(f"请求 Danbooru 异常: {e}")
    return None

def send_telegram(img_url):
    quote_text = get_daily_quote()
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = f"{quote_text}\n\n🏐 <b>每日日向翔阳</b>\n#Haikyuu #HinataShoyo"

    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    
    try:
        print("正在推送给 Telegram...")
        res = requests.post(send_url, data=payload, timeout=10)
        print(f"Telegram 推送状态: {res.status_code}")
        if res.status_code != 200:
            print(f"推送失败原因: {res.text}")
    except Exception as e:
        print(f"发送异常: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("致命错误：Secrets 未配置！")
    else:
        print("=== 任务开始 ===")
        pic = get_hinata_image()
        
        if pic:
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            # 让 Action 显示为失败（红色），方便你收到通知
            exit(1)
