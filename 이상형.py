import streamlit as st
import random

# 데이터: 항목 + 성향 결과
candidates = {
    "강아지": "❤️ 따뜻하고 충성심 강한 사람입니다. 감정에 솔직하고 사람을 좋아해요.",
    "고양이": "🧠 독립적이고 조용한 성향! 자기만의 시간과 공간이 중요합니다.",
    "햄버거": "🔥 즉흥적이고 활동적인 타입! 일단 도전부터 하는 스타일이에요.",
    "초밥": "🌊 섬세하고 깔끔한 감각의 소유자! 조용히 중심을 잡는 타입.",
    "바다": "🌴 자유와 휴식을 사랑하는 자연친화형 성격!",
    "산": "🧘 내면이 깊고 안정 지향적이에요. 성실한 편입니다.",
    "책": "📚 지적인 성향이 강하고 호기심이 많아요!",
    "게임기": "🎮 상상력이 풍부하고 즐거움을 추구하는 타입!",
    "커피": "☕ 감성적이고 분위기를 중시하는 낭만파!",
    "에너지드링크": "⚡ 빠르게 움직이고 집중력이 강해요. 성취 지향형!",
    "강아지 인형": "💗 귀엽고 부드러운 감성을 가진 사람입니다.",
    "고릴라": "💪 강한 정신력과 리더십이 있는 현실적인 타입!",
    "우주": "🪐 철학적이고 꿈 많은 사람입니다. 상상력이 풍부해요.",
    "꽃": "🌸 감성적이고 따뜻한 에너지! 사람을 잘 챙겨요.",
    "시계": "⏰ 시간 개념 철저! 계획적이고 논리적인 사람.",
    "롤러코스터": "🎢 짜릿한 걸 즐기는 흥미 위주 탐색형입니다!"
}

# 초기화
if "current" not in st.session_state:
    st.session_state.current = list(candidates.keys())
    random.shuffle(st.session_state.current)
    st.session_state.round = 1

st.set_page_config(page_title="이상형 월드컵 심리게임", layout="centered")
st.title("🧠 이상형 월드컵 - 심리 성향 테스트")

# 종료 조건
if len(st.session_state.current) == 1:
    final = st.session_state.current[0]
    st.success(f"🎉 당신의 선택은: **{final}**")
    st.markdown(f"💬 성향 분석: {candidates[final]}")
    if st.button("🔄 다시 시작하기"):
        for key in ["current", "round"]:
            st.session_state.pop(key)
        st.experimental_rerun()
    st.stop()

# 현재 라운드 표시
st.markdown(f"### 🔥 {len(st.session_state.current)}강 - Round {st.session_state.round}")

# 두 개씩 비교
pair = st.session_state.current[:2]
col1, col2 = st.columns(2)
if col1.button(pair[0]):
    st.session_state.current = st.session_state.current[2:] + [pair[0]]
    st.session_state.round += 1
    st.experimental_rerun()
if col2.button(pair[1]):
    st.session_state.current = st.session_state.current[2:] + [pair[1]]
    st.session_state.round += 1
    st.experimental_rerun()
