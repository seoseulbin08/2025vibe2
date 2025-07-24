import streamlit as st
import numpy as np

# 미로 맵 정의 (0: 길, 1: 벽)
maze = np.array([
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,0,1,0,1,0,1],
    [1,0,0,1,0,1,0,0,0,1],
    [1,0,0,0,0,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,0,1],
])

start = (1, 1)
goal = (8, 9)

# 상태 저장
if "player_pos" not in st.session_state:
    st.session_state.player_pos = start
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.set_page_config(page_title="미로 탈출 게임", layout="centered")
st.title("🧩 Streamlit 미로 탈출 게임")

# 승리 조건
if st.session_state.player_pos == goal:
    st.success("🎉 미로 탈출 성공!")
    st.session_state.game_over = True

# 미로 표시 함수
def draw_maze():
    grid = ""
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if (i, j) == st.session_state.player_pos:
                grid += "🟦"
            elif (i, j) == goal:
                grid += "🟩"
            elif maze[i][j] == 1:
                grid += "⬛"
            else:
                grid += "⬜"
        grid += "\n"
    st.markdown(f"<pre style='font-size:20px'>{grid}</pre>", unsafe_allow_html=True)

draw_maze()

# 이동 함수
def move(dx, dy):
    if st.session_state.game_over:
        return
    x, y = st.session_state.player_pos
    nx, ny = x + dx, y + dy
    if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1]:
        if maze[nx][ny] == 0:
            st.session_state.player_pos = (nx, ny)

# 버튼 UI
col1, col2, col3 = st.columns(3)
with col2:
    st.button("⬆️ 위", on_click=move, args=(-1, 0))
col1, col2, col3 = st.columns(3)
with col1:
    st.button("⬅️ 왼쪽", on_click=move, args=(0, -1))
with col2:
    st.button("⬇️ 아래", on_click=move, args=(1, 0))
with col3:
    st.button("➡️ 오른쪽", on_click=move, args=(0, 1))

# 리셋 버튼
if st.button("🔄 게임 다시 시작"):
    st.session_state.player_pos = start
    st.session_state.game_over = False
