# kart_game.py
import streamlit as st
import random

# 세션 상태 초기화
if "distance" not in st.session_state:
    st.session_state.distance = 0
if "speed" not in st.session_state:
    st.session_state.speed = 10
if "item" not in st.session_state:
    st.session_state.item = None
if "log" not in st.session_state:
    st.session_state.log = []

# 제목
st.set_page_config(page_title="카트 미니게임", layout="centered")
st.title("🏎️ 미니 카트 게임 - 결승선을 향해!")

# 진행률 표시
st.progress(min(st.session_state.distance, 100) / 100, text=f"📍 현재 진행률: {st.session_state.distance}%")

# 현재 상태
st.write(f"🚗 현재 속도: {st.session_state.speed} / 최대 30")
if st.session_state.item:
    st.write(f"🎁 보유 아이템: `{st.session_state.item}`")

# 로그 출력
with st.expander("📜 주행 로그 보기"):
    for log in reversed(st.session_state.log[-10:]):
        st.write(log)

# 주행 버튼
if st.button("➡️ 주행!"):
    event = random.choice([
        "부스터 획득!", "바나나 밟음!", "속도 유지", "아이템 박스 획득", "장애물 충돌!", "부스트 구간 통과!", "미끄러운 턴 구간"
    ])

    # 거리 증가
    gain = st.session_state.speed
    st.session_state.distance += gain
    st.session_state.distance = min(100, st.session_state.distance)

    # 이벤트 처리
    if event == "부스터 획득!":
        st.session_state.speed = min(30, st.session_state.speed + 10)
        st.session_state.log.append("🚀 부스터 획득! 속도 +10")
    elif event == "바나나 밟음!":
        st.session_state.speed = max(5, st.session_state.speed - 10)
        st.session_state.log.append("🍌 바나나 밟음... 속도 -10")
    elif event == "속도 유지":
        st.session_state.log.append("😐 아무 일도 일어나지 않았어요.")
    elif event == "아이템 박스 획득":
        item = random.choice(["물풍선", "자석", "부스터", "지뢰"])
        st.session_state.item = item
        st.session_state.log.append(f"🎁 아이템 박스! `{item}` 획득")
    elif event == "장애물 충돌!":
        st.session_state.speed = max(5, st.session_state.speed - 15)
        st.session_state.log.append("💥 장애물 충돌! 속도 -15")
    elif event == "부스트 구간 통과!":
        st.session_state.speed = min(30, st.session_state.speed + 5)
        st.session_state.log.append("🔥 부스트 구간! 속도 +5")
    elif event == "미끄러운 턴 구간":
        st.session_state.speed = max(5, st.session_state.speed - 5)
        st.session_state.log.append("🌀 미끄러운 턴! 속도 -5")

    # 도착 처리
    if st.session_state.distance >= 100:
        st.success("🎉 결승선 도착! 완주 성공!")
        st.balloons()

# 아이템 사용 버튼
if st.session_state.item:
    if st.button("🎯 아이템 사용"):
        msg = ""
        if st.session_state.item == "물풍선":
            st.session_state.speed = max(5, st.session_state.speed - 5)
            msg = "💦 물풍선 사용! 상대방 속도가 느려졌어요 (당신도 살짝 미끄러짐)"
        elif st.session_state.item == "자석":
            st.session_state.speed = min(30, st.session_state.speed + 5)
            msg = "🧲 자석 사용! 앞차의 속도를 흡수했어요"
        elif st.session_state.item == "부스터":
            st.session_state.speed = min(30, st.session_state.speed + 15)
            msg = "💨 부스터 사용! 속도 +15"
        elif st.session_state.item == "지뢰":
            st.session_state.speed = max(5, st.session_state.speed - 10)
            msg = "💣 지뢰 설치 후 자폭했어요... 속도 -10"

        st.session_state.log.append(msg)
        st.session_state.item = None

# 초기화 버튼
if st.button("🔄 게임 리셋"):
    st.session_state.distance = 0
    st.session_state.speed = 10
    st.session_state.item = None
    st.session_state.log = []
    st.success("🏁 게임이 초기화되었습니다!")
