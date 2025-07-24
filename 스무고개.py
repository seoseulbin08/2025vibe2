# file: twenty_questions.py
import streamlit as st
import openai

# 🔑 OpenAI API 키 입력
openai.api_key = st.secrets["OPENAI_API_KEY"]  # 또는 직접 입력해도 됨

# 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": "너는 사용자가 마음속에 떠올린 사물을 맞추기 위한 AI야. "
                   "너는 최대 20개의 질문만 할 수 있어. 질문은 하나씩 차례대로 해. "
                   "사용자의 응답은 '예', '아니오', '잘 모르겠어요' 중 하나야. "
                   "가능하면 중간에 정답을 유추해서 자신 있게 말해. "
                   "사용자가 맞다고 하면 '정답이야!'라고 외쳐!"
    }]
    st.session_state.turns = 0
    st.session_state.finished = False

# 타이틀
st.set_page_config(page_title="20 Questions", layout="centered")
st.title("🧠 20 Questions - AI가 당신의 생각을 맞춰볼게!")

# 안내문
if st.session_state.turns == 0:
    st.info("사물, 동물, 유명인 등 **무엇이든 하나 떠올려 주세요.**\n\n준비되면 아래 질문을 시작하세요.")

# 대화 표시
for m in st.session_state.messages[1:]:  # system 제외
    role = "🤖 GPT" if m["role"] == "assistant" else "🙋 당신"
    st.chat_message(role).write(m["content"])

# GPT 질문 출력
if not st.session_state.finished and st.session_state.turns < 20:
    with st.chat_message("🤖 GPT"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 필요하면 gpt-4로 변경
            messages=st.session_state.messages
        )
        question = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.write(question)

    # 사용자 응답
    user_reply = st.radio("당신의 응답은?", ["예", "아니오", "잘 모르겠어요"], key=st.session_state.turns)
    if st.button("응답 보내기"):
        st.session_state.messages.append({"role": "user", "content": user_reply})
        st.session_state.turns += 1
        st.experimental_rerun()

# 종료 조건
if st.session_state.turns >= 20 and not st.session_state.finished:
    st.warning("❌ AI가 20번 안에 정답을 못 맞췄어요. 당신이 생각한 건 무엇이었나요?")
    final_answer = st.text_input("정답을 알려주세요!")
    if st.button("정답 제출"):
        st.success("게임 끝! 다음에 다시 도전해볼게요 😎")
        st.session_state.finished = True
