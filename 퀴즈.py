# file: simple_twenty_questions.py
import streamlit as st
import random

# 질문 리스트 (최대 20개)
questions = [
    "그것은 살아 있나요?",
    "그것은 동물인가요?",
    "그것은 전기를 사용하나요?",
    "그것은 자동차인가요?",
    "그것은 보통 집 안에 있나요?",
    "그것은 크기가 책상보다 작나요?",
    "그것은 소리를 내나요?",
    "그것은 기술 제품인가요?",
    "그것은 음식인가요?",
    "그것은 하늘을 날 수 있나요?",
    "그것은 바퀴가 있나요?",
    "그것은 물에서 사용되나요?",
    "그것은 여러분이 만져볼 수 있나요?",
    "그것은 학교에서 볼 수 있나요?",
    "그것은 빨간색일 수 있나요?",
    "그것은 유명한 캐릭터인가요?",
    "그것은 영화에 나온 적이 있나요?",
    "그것은 동물원에서 볼 수 있나요?",
    "그것은 나무로 만들어졌나요?",
    "그것은 무겁나요?"
]

# 추측 후보 리스트 (정답은 사용자가 마음속으로 정함)
guesses = [
    "강아지", "고양이", "자동차", "의자", "TV", "핸드폰",
    "비행기", "냉장고", "토스터기", "펭귄", "기린", "사자",
    "햄버거", "수박", "의사", "아이언맨", "해리포터", "버스", "책", "우산"
]

# 세션 상태 초기화
if "turn" not in st.session_state:
    st.session_state.turn = 0
    st.session_state.answers = []
    st.session_state.finished = False
    st.session_state.final_guess = ""

st.set_page_config(page_title="스무고개", layout="centered")
st.title("🧠 스무고개 (20 Questions)")

# 질문 진행
if not st.session_state.finished and st.session_state.turn < len(questions):
    q = questions[st.session_state.turn]
    st.subheader(f"Q{st.session_state.turn + 1}: {q}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("예 😊"):
            st.session_state.answers.append("예")
            st.session_state.turn += 1
            st.experimental_rerun()
    with col2:
        if st.button("아니오 🙅"):
            st.session_state.answers.append("아니오")
            st.session_state.turn += 1
            st.experimental_rerun()
    with col3:
        if st.button("잘 모르겠어요 🤔"):
            st.session_state.answers.append("모름")
            st.session_state.turn += 1
            st.experimental_rerun()

# 추측 출력
elif not st.session_state.finished:
    st.subheader("🕵️ 이제 내가 한 번 맞춰볼게...")
    # 단순하게 무작위 추측
    st.session_state.final_guess = random.choice(guesses)
    st.write(f"내 추측은... **{st.session_state.final_guess}**!")

    if st.button("정답이야! 🎉"):
        st.success("🎯 맞췄다! 나는 천재야 😎")
        st.session_state.finished = True
    elif st.button("틀렸어 ❌"):
        st.warning("에잉... 다음엔 더 잘 맞출게!")
        st.session_state.finished = True

# 게임 다시 시작
if st.session_state.finished:
    if st.button("🔄 다시 시작하기"):
        for key in ["turn", "answers", "finished", "final_guess"]:
            st.session_state.pop(key, None)
        st.experimental_rerun()
