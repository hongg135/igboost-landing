# writer.py
import openai
import os

# ✅ 設定 GROQ API Key 與 endpoint
openai.api_key = os.getenv("GROQ_API_KEY", "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")
openai.api_base = "https://api.groq.com/openai/v1"

def generate_ig_captions(topic: str):
    prompt = f"""
你是一位專業的 IG 行銷文案創作者。
主題是：{topic}
請你針對這個主題，產出三種不同風格的 IG 發文文案，每種都附上合適的 Hashtag。

請以以下格式輸出：
【風格一】XXX
Hashtags: #xxx #yyy

【風格二】XXX
Hashtags: #aaa #bbb

【風格三】XXX
Hashtags: #ccc #ddd
"""

    response = openai.ChatCompletion.create(
        model="llama3-70b-8192",  # GROQ 支援的模型
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    content = response['choices'][0]['message']['content']
    return content
