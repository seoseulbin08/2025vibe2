import streamlit as st

# 샘플 코디 데이터 (조건 기반 추천)
outfit_db = {
    ("여성", "20대", "맑음", "데이트", "러블리"): {
        "image": "https://i.imgur.com/ZC3HRbK.jpg",  # 예시 이미지
        "description": "하늘하늘한 원피스에 흰색 샌들, 미니 핸드백을 매치해보세요. 로맨틱한 분위기에 잘 어울려요!",
    },
    ("남성", "30대", "비", "출근", "포멀"): {
        "image": "https://i.imgur.com/Bj4N6l7.jpg",
        "description": "그레이 정장에 방수 트렌치코트, 짙은색 로퍼를 추천해요. 비 오는 날엔 신발 방수도 중요해요.",
    },
    ("여성", "10대", "더움", "학교", "캐주얼"): {
        "image": "https://i.imgur.com/V2BlhB1.jpg",
        "description": "반팔 티셔츠에 데님 반바지, 스니커즈! 백팩과 함께 활동성도 챙기자!",
    },
    # 추가적으로 조건 조합 더 넣을 수 있음
}

# Streamlit UI
st.title("👗 AI 옷 코디 추천기")
st.markdown("너의 상황에 딱 맞는 오늘의 코디를 추천해줄게!")

with st.form("input_form"):
    gender = st.selectbox("성별", ["여성", "남성"])
    age = st.selectbox("나이대", ["10대", "20대", "30대", "40대 이상"])
    weather = st.selectbox("날씨", ["맑음", "흐림", "비", "눈", "더움", "추움"])
    situation = st.selectbox("상황", ["학교", "데이트", "출근", "면접", "여행", "집콕"])
    style = st.selectbox("스타일", ["캐주얼", "러블리", "스트릿", "포멀", "꾸안꾸"])

    submitted = st.form_submit_button("코디 추천받기")

if submitted:
    key = (gender, age, weather, situation, style)
    outfit = outfit_db.get(key)

    if outfit:
        st.image(outfit["image"], use_column_width=True)
        st.success(outfit["description"])
    else:
        st.warning("이 조합에 맞는 코디가 아직 없어요. 조건을 다르게 바꿔보세요!")

