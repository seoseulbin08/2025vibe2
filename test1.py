# app.py
import streamlit as st
import random

# ----------------------------
# 설정
st.set_page_config(page_title="AI 옷 코디 추천기", layout="centered")
st.title("🧥 AI 옷 코디 추천기")

st.sidebar.header("당신에 대해 알려주세요")

# ----------------------------
# 사용자 입력
gender = st.sidebar.selectbox("성별", ["여성", "남성"])
age = st.sidebar.selectbox("나이대", ["10대", "20대", "30대", "40대 이상"])
weather = st.sidebar.selectbox("오늘 날씨", ["맑음", "흐림", "비", "눈", "더움", "추움"])
situation = st.sidebar.selectbox("상황/장소", ["학교", "데이트", "직장", "면접", "여행", "집콕"])
style = st.sidebar.selectbox("스타일", ["캐주얼", "스트릿", "러블리", "포멀", "꾸안꾸", "미니멀"])

if st.sidebar.button("코디 추천 받기"):
    
    # ----------------------------
    # 간단한 코디 조합 예시
    outfits = {
        "여성": {
            "캐주얼": [
                {"text": "흰 티셔츠에 청바지, 흰 스니커즈 조합은 언제나 깔끔해요.",
                 "image": "https://i.imgur.com/2d1h1lZ.jpg"},
                {"text": "크롭 니트와 와이드 팬츠, 캔버스화 조합 추천!",
                 "image": "https://i.imgur.com/Xd03qoc.jpg"}
            ],
            "러블리": [
                {"text": "플로럴 원피스에 니트 가디건, 플랫슈즈를 매치해보세요.",
                 "image": "https://i.imgur.com/5O68vh7.jpg"},
                {"text": "하늘색 블라우스에 A라인 스커트 조합, 데이트에 좋아요!",
                 "image": "https://i.imgur.com/Exa82IQ.jpg"}
            ]
        },
        "남성": {
            "스트릿": [
                {"text": "오버핏 맨투맨 + 조거팬츠 + 나이키 덩크 조합 추천!",
                 "image": "https://i.imgur.com/W1X2psJ.jpg"},
                {"text": "그래픽 티셔츠에 와이드 청바지, 비니로 포인트!",
                 "image": "https://i.imgur.com/M3z0mCJ.jpg"}
            ],
            "포멀": [
                {"text": "네이비 셔츠에 슬랙스, 브라운 로퍼로 깔끔한 직장룩 완성.",
                 "image": "https://i.imgur.com/1rk7tuK.jpg"},
                {"text": "그레이 수트에 흰 셔츠, 블랙 옥스포드화 추천!",
                 "image": "https://i.imgur.com/7KMlm7h.jpg"}
            ]
        }
    }

    # 예외 처리: 스타일이 없는 경우 캐주얼 기본값
    gender_outfits = outfits.get(gender, {})
    style_outfits = gender_outfits.get(style, outfits[gender]["캐주얼"])
    selected = random.choice(style_outfits)

    # ----------------------------
    # 결과 출력
    st.subheader("👗 추천 코디")
    st.write(selected["text"])
    st.image(selected["image"], caption="추천 이미지", use_container_width=True)

    # 팁 출력
    if weather in ["비", "눈"]:
        st.info("💡 우산 또는 방수 아이템을 챙기는 걸 잊지 마세요!")
    elif weather == "더움":
        st.info("💡 땀흡수 잘 되는 소재나 밝은 색상 옷을 추천해요!")
    elif weather == "추움":
        st.info("💡 보온성 있는 이너와 아우터를 꼭 챙기세요!")


