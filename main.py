import requests
import os
import random

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. 获取“一言”语录 (API)
def get_daily_quote():
    # 这是一个免费的公开接口
    # 参数 c=a 表示动画，c=b 表示漫画，c=d 表示文学，c=k 表示哲学
    # 我们这里混合请求：动画、漫画、哲学，希望能随机到热血或有深度的句子
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    
    try:
        res = requests.get(api_url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            # 获取句子内容
            content = data.get('hitokoto')
            # 获取出处 (比如是哪部动漫)
            source = data.get('from')
            
            # 组合成一句完整的话
            return f"“{content}”\n——《{source}》"
    except Exception as e:
        print(f"获取语录失败: {e}")
    
    # 如果接口挂了，或者网络不好，返回这句保底
    return "“因为想赢，所以才会战斗！”\n——《排球少年！！》"

def get_hinata_image():
    # 依然使用 Safebooru + Pixiv 标签
    url = "https://safebooru.donmai.us/posts.json?tags=hinata_shouyou+pixiv+rating:general&limit=20"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            posts = response.json()
            if posts:
                post = random.choice(posts)
                return post.get('file_url') or post.get('sample_url')
    except Exception as e:
        print(f"获取图片出错: {e}")
    return None

def send_telegram(img_url):
    if not img_url:
        print("未找到图片，跳过发送")
        return

    # === 获取今日语录 ===
    quote_text = get_daily_quote()

    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    
    # 构造消息内容
    caption_text = (
        f"{quote_text}\n\n"
        f"🏐 <b>每日日向翔阳</b>\n"
        f"#Haikyuu #HinataShoyo"
    )

    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    
    try:
        res = requests.post(send_url, data=payload, timeout=10)
        print(f"推送状态: {res.status_code}")
    except Exception as e:
        print(f"发送消息异常: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("错误：请检查 Secrets 设置")
    else:
        print("开始运行...")
        pic = get_hinata_image()
        if pic:
            send_telegram(pic)
