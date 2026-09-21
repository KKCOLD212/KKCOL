import streamlit as st
import requests

st.set_page_config(page_title="Для тебя", page_icon="❤️", layout="centered")

st.markdown("""
    <style>
    .main-text { font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 30px; }
    .heart { font-size: 100px; text-align: center; animation: pulse 1s infinite alternate; }
    @keyframes pulse { from { transform: scale(1); } to { transform: scale(1.2); } }
    .stButton>button { width: 100%; font-size: 18px; }
    </style>
""", unsafe-allow_html=True)

if 'choice' not in st.session_state:
    st.session_state.choice = None

# СЮДА ВСТАВЬТЕ СВОИ ДАННЫЕ ИЗ ТЕЛЕГРАМА:
TELEGRAM_TOKEN = "ВАШ_ТОКЕН_БОТА"
TELEGRAM_CHAT_ID = "ВАШ_ID_ЧАТА"

def send_telegram_message(text):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://telegram.org{TELEGRAM_TOKEN}/sendMessage"
        try:
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
        except:
            pass

if st.session_state.choice is None:
    st.markdown('<p class="main-text">Привет, я до сих пор тебя люблю. Давай хотя бы попробуем?</p>', unsafe-allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Да", type="primary"):
            st.session_state.choice = "yes"
            send_telegram_message("Она сказала ДА! ❤️")
            st.rerun()
    with col2:
        if st.button("Нет"):
            st.session_state.choice = "no"
            send_telegram_message("Она сказала нет... 💔")
            st.rerun()
elif st.session_state.choice == "yes":
    st.markdown('<p class="heart">❤️</p>', unsafe-allow_html=True)
    st.balloons()
elif st.session_state.choice == "no":
    st.markdown('<p class="main-text">И даже после всего что я для тебя сделал?</p>', unsafe-allow_html=True)
