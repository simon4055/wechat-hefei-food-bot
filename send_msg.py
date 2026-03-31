import requests
import json

# ========== 这里改成你的语鲸配置 ==========
WHALE_WEBHOOK = "【粘贴你的语鲸频道推送Webhook】"
CHANNEL_NAME = "合肥美食密码"
MSG_TITLE = "每日美食推送｜晚间18点定时更新"
MSG_CONTENT = """
今日合肥精选美食推荐：
1. 本地特色豆制品/小吃上新
2. 小众宝藏咖啡店/手冲店打卡
3. 周边城市美食攻略同步更新

订阅链接：https://lingowhale.com/s/RuF4qOd
"""
# ======================================

def send_wechat_msg():
    payload = {
        "title": MSG_TITLE,
        "content": MSG_CONTENT,
        "channel": CHANNEL_NAME
    }
    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(WHALE_WEBHOOK, data=json.dumps(payload), headers=headers, timeout=15)
        print("推送成功！返回结果：", res.text)
    except Exception as e:
        print("推送失败：", str(e))

if __name__ == "__main__":
    send_wechat_msg()
