# rps_game_final.py
import streamlit as st
import random
import time

# 점수 저장용 session_state 초기화
if "win" not in st.session_state:
    st.session_state.win = 0
if "draw" not in st.session_state:
    st.session_state.draw = 0
if "lose" not in st.session_state:
    st.session_state.lose = 0

# 🩷 핑크 스타일 설정
st.set_page_config(page_title="핑크 가위바위보", layout="centered")
st.markdown("""
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
.score-box {
    background-color: #fff0f5;
    border: 2px solid #ffb6c1;
    padding: 10px;
    border-radius: 12px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# 🎀 제목
st.markdown("<h1>🎀 가위바위보 게임 🎀</h1>", unsafe_allow_html=True)

# 🎯 점수판 표시
st.markdown("<div class='score-box'><h2>🏆 점수판</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("승리", st.session_state.win)
col2.metric("무승부", st.session_state.draw)
col3.metric("패배", st.session_state.lose)
st.markdown("</div>", unsafe_allow_html=True)

# 🎮 사용자 선택
choices = ["가위", "바위", "보"]
user_choice = st.radio("당신의 선택은?", choices, horizontal=True)

# 🕹️ 대결 버튼
if st.button("대결 시작!"):
    st.subheader("⏳ 준비 중...")

    # 3,2,1 카운트다운
    countdown = st.empty()
    for i in range(3, 0, -1):
        countdown.markdown(f"<h2>{i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)

    countdown.markdown("<h2>💖 가자!</h2>", unsafe_allow_html=True)
    time.sleep(0.6)
    countdown.empty()

    # 컴퓨터 고민 중
    thinking = st.empty()
    thinking.markdown("<h2>🤔 컴퓨터가 고민 중...</h2>", unsafe_allow_html=True)
    time.sleep(1.3)
    thinking.empty()

    # 컴퓨터 선택
    computer_choice = random.choice(choices)

    # 결과 판단
    if user_choice == computer_choice:
        result = "비겼어요! 😐"
        st.session_state.draw += 1
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "이겼어요! 🥳"
        st.session_state.win += 1
    else:
        result = "졌어요... 😢"
        st.session_state.lose += 1

    # 결과 출력
    st.markdown("---")
    st.markdown(f"<h2>당신의 선택: {user_choice}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2>컴퓨터의 선택: {computer_choice}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)

    # 이펙트
    if "이겼" in result:
        st.balloons()
    elif "졌" in result:
        st.snow()
