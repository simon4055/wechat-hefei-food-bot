import requests
import json

# ======================
# 你的配置（已全部填好）
# ======================
WXPUSH_URL = "https://wxpush-hefei-food.56343418.workers.dev"
API_TOKEN = "hefei_food_push_2026_C@rref0ur"
LINGOWHALE_URL = "https://lingowhale.com/s/RuF4qOd"

def send_to_wechat():
    # ==============================================
    # 这里就是你要推送到微信的【真实内容】
    # 想改内容直接在这里改就行！
    # ==============================================
    title = "合肥美食密码｜每日18点推送"
    
    content = """【今日合肥美食推荐】
1. 老合肥正宗淮南牛肉汤，鲜香暖胃
2. 本地特色徽式小吃，地道风味
3. 网红甜品店新品上线
4. 合肥各区隐藏美食小店打卡

每天定时更新，带你吃遍合肥~
"""

    # 推送
    data = {
        "api_token": API_TOKEN,
        "title": title,
        "content": content,
        "link": LINGOWHALE_URL
    }

    try:
        res = requests.post(WXPUSH_URL, json=data, timeout=15)
        print("✅ 推送成功！")
        print("返回结果：", res.text)
    except Exception as e:
        print("❌ 推送失败：", e)

if __name__ == "__main__":
    send_to_wechat()
