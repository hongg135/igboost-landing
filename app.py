import streamlit as st
from writer import generate_ig_captions
from telegram_bot import send_telegram_message

st.set_page_config(page_title="IG 文案產生器", layout="centered")

st.title("📱 IG 文案產生器")
st.markdown("輸入主題，產出多種風格文案與標籤，適用於行銷、貼文、社群推廣。")

topic = st.text_input("請輸入主題", placeholder="例如：寵物插畫、咖啡廳、美妝保養")

if st.button("產生文案") and topic:
    with st.spinner("正在產生文案..."):
        try:
            results = generate_ig_captions(topic)
            st.success("文案產生完成 🎉")
            for i, result in enumerate(results, 1):
                st.markdown(f"### 風格 {i}")
                st.markdown(result)
            
            # 發送 Telegram 通知
            send_telegram_message(f"✅ IG 文案產生成功！主題：{topic}")
        except Exception as e:
            st.error("文案產生失敗，請稍後再試。")
            send_telegram_message(f"❌ IG 文案產生失敗。\n錯誤訊息：{str(e)}")
