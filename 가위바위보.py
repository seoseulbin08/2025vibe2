# rps_game_thinking.py
import streamlit as st
import random
import time

# 🩷 페이지 설정
st.set_page_config(page_title="핑크 가위바위보", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f0;
    }
    .stApp {
        background-color: #ffe6f0;
    }
    h1, h2 {
        color: #d63384;
        text-align: center;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #ff69b4;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🎀 가위바위보 게임 🎀</h1>", unsafe_allow_html=True)

# 🎮 사용자 선택
choices = ["가위", "바위", "보"]
user_choice = st.radio("당신의 선택은?", choices, horizontal=True)

# 🕹️ 게임 실행
if st.button("대결 시작!"):
    st.subheader("⏳ 준비 중...")

    # 카운트다운
    countdown = st.empty()
    for i in range(3, 0, -1):
        countdown.markdown(f"<h2>{i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)

    countdown.markdown("<h2>👊 가자!</h2>", unsafe_allow_html=True)
    time.sleep(0.5)

    # 컴퓨터 고민 중 출력
    thinking = st.empty()
    thinking.markdown("<h2>🤔 컴퓨터가 고민 중...</h2>", unsafe_allow_html=True)
    time.sleep(1.5)
    thinking.empty()

    # 컴퓨터 선택
    computer_choice = random.choice(choices)

    # 승패 판단
    if user_choice == computer_choice:
        result = "비겼어요! 😐"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "이겼어요! 🥳"
    else:
        result = "졌어요... 😢"

    # 결과 출력
    st.markdown("---")
    st.markdown(f"<h2>당신의 선택: {user_choice}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2>컴퓨터의 선택: {computer_choice}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)

    # 효과
    if "이겼" in result:
        st.balloons()
    elif "졌" in result:
        st.snow()
