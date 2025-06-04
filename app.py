import streamlit as st
from writer import generate_ig_captions
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="IG 文案生成器", layout="centered")

st.title("📱 IG 文案生成器")
topic = st.text_input("請輸入主題（例：貓咪、旅遊、美食...）")

if st.button("產生文案") and topic:
    with st.spinner("生成中..."):
        results = generate_ig_captions(topic)
        st.success("已生成！")
        st.write(results)
