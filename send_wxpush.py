import requests
import json
import re

# ======================
# 你的配置（已填好）
# ======================
WXPUSH_URL = "https://wxpush-hefei-food.56343418.workers.dev"
API_TOKEN = "hefei_food_push_2026_C@rref0ur"
LINGOWHALE_URL = "https://lingowhale.com/s/RuF4qOd"

def get_lingowhale_content():
    """自动抓取语鲸最新一篇文章的标题和内容"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36"
        }
        resp = requests.get(LINGOWHALE_URL, headers=headers, timeout=10)
        html = resp.text

        # 抓取第一篇文章标题
        title_match = re.search(r'<h3.*?>(.*?)</h3>', html, re.S)
        article_title = title_match.group(1).strip() if title_match else "合肥美食推荐"

        # 抓取文章简介/内容
        content_match = re.search(r'<p.*?class="summary".*?>(.*?)</p>', html, re.S)
        article_content = content_match.group(1).strip() if content_match else "今日美食上新啦~"

        # 清理HTML标签
        article_content = re.sub(r'<.*?>', '', article_content)

        return article_title, article_content

    except Exception as e:
        print("抓取失败：", e)
        return "合肥美食密码｜每日推送", "今日精选美食已更新"

def send_to_wechat(title, content):
    data = {
        "api_token": API_TOKEN,
        "title": title,
        "content": content,
        "link": LINGOWHALE_URL
    }
    res = requests.post(WXPUSH_URL, json=data, timeout=15)
    print("推送成功", res.text)

# 执行
if __name__ == "__main__":
    title, content = get_lingowhale_content()
    send_to_wechat(title, content)
