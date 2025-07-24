# number_baseball_game.py
import streamlit as st
import random

# 함수: 3자리 정답 생성
def generate_answer():
    digits = list(range(0, 10))
    random.shuffle(digits)
    return digits[:3]

# 함수: 입력 유효성 검사
def is_valid_input(user_input):
    return (
        user_input.isdigit()
        and len(user_input) == 3
        and len(set(user_input)) == 3
    )

# 함수: 스트라이크 & 볼 판정
def get_score(answer, guess):
    s = 0
    b = 0
    for i in range(3):
        if guess[i] == answer[i]:
            s += 1
        elif guess[i] in answer:
            b += 1
    return s, b

# 초기화
st.set_page_config(page_title="숫자 야구 게임", layout="centered")
st.title("⚾ 숫자 야구 게임 (3자리 숫자 맞히기!)")

# 상태 저장
if "answer" not in st.session_state:
    st.session_state.answer = generate_answer()
    st.session_state.tries = []
    st.session_state.game_over = False

# 게임 종료 후 재시작
if st.session_state.game_over:
    if st.button("🔄 다시 시작하기"):
        st.session_state.answer = generate_answer()
        st.session_state.tries = []
        st.session_state.game_over = False
    st.stop()

# 사용자 입력
user_input = st.text_input("세 자리 숫자를 입력하세요 (중복X):", max_chars=3)

if st.button("확인"):
    if not is_valid_input(user_input):
        st.warning("⚠️ 유효한 3자리 숫자를 입력하세요! (숫자만, 중복X)")
    else:
        guess = [int(d) for d in user_input]
        s, b = get_score(st.session_state.answer, guess)
        st.session_state.tries.append((user_input, s, b))

        if s == 3:
            st.success(f"🎉 정답입니다! 정답은 {''.join(map(str, st.session_state.answer))} 입니다!")
            st.balloons()
            st.session_state.game_over = True
        else:
            st.info(f"👉 {user_input} → {s}S {b}B")

# 시도 기록 출력
if st.session_state.tries:
    st.markdown("### 📝 시도 기록")
    for attempt, s, b in reversed(st.session_state.tries):
        st.write(f"➡️ {attempt} → {s}S {b}B")
