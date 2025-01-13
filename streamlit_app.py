import streamlit as st
from streamlit_chat import message
import requests

# Địa chỉ API Flask
API_URL = "http://localhost:5000/inference"

st.title("Chatbot Flan-T5")

# Hiển thị tin nhắn mặc định
message("Hi, I am Flan-T5 Chatbot. How can I help you?", is_user=False)

# Placeholder để hiển thị lịch sử chat
placeholder = st.empty()
user_input = st.text_input("Human")

if st.button("Send"):
    with placeholder.container():
        message(user_input, is_user=True)

    # Gửi yêu cầu tới Flask API
    with st.spinner("Generating Response..."):
        response = requests.post(API_URL, json={"input_text": "Human: " + user_input + ". Assistant: "})
        if response.status_code == 200:
            bot_response = response.json().get("response", "")
        else:
            bot_response = "Error: Unable to connect to backend."

    with placeholder.container():
        message(bot_response, is_user=False)
