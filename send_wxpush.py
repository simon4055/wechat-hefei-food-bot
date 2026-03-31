import requests
import json

# ======================
# 只需要改这 2 个地方！
# ======================
WXPUSH_URL = "https://wxpush-hefei-food.56343418.workers.dev"
API_TOKEN = "hefei_food_push_2026_C@rref0ur"

def send():
    data = {
        "api_token": API_TOKEN,
        "title": "合肥美食密码｜每日18点推送",
        "content": "1. 本地特色小吃上新\n2. 小众咖啡店推荐\n3. 周边美食攻略更新",
        "link": "https://lingowhale.com/s/RuF4qOd"
    }

    try:
        response = requests.post(WXPUSH_URL, json=data, timeout=15)
        print("推送成功！返回：", response.text)
    except Exception as e:
        print("推送失败：", e)

if __name__ == "__main__":
    send()
