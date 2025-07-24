# rps_game_animated.py
import streamlit as st
import random
import time

st.set_page_config(page_title="가위바위보 게임", layout="centered")
st.title("✂️✊🖐️ 가위바위보 게임")

# 선택 옵션
choices = ["가위", "바위", "보"]

# 사용자 선택
user_choice = st.radio("당신의 선택은?", choices, horizontal=True)

# 버튼 누르면 게임 실행
if st.button("대결 시작!"):
    st.subheader("🔄 준비 중...")

    # 애니메이션 효과: 3, 2, 1
    countdown_text = st.empty()
    for i in range(3, 0, -1):
        countdown_text.markdown(f"<h2 style='text-align:center;'>⏳ {i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)

    countdown_text.markdown("<h2 style='text-align:center;'>👊 가자!</h2>", unsafe_allow_html=True)
    time.sleep(0.5)

    # 컴퓨터 선택
    computer_choice = random.choice(choices)

    # 결과 판단
    if user_choice == computer_choice:
        result = "비겼어요! 😐"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "이겼어요! 🥳"
    else:
        result = "졌어요... 😢"

    # 결과 출력
    st.subheader("🎮 결과")
    st.write(f"당신: **{user_choice}**")
    st.write(f"컴퓨터: **{computer_choice}**")
    st.success(result if "이겼" in result else result)
