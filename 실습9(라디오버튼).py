#라디오 버튼

import streamlit as st

# page_title 페이지 제목 설정
st.set_page_config(page_title = '홈페이지',
                   page_icon = ':sunglasses:')

# 이후 Streamlit 명령어 사용
st.title('라디오 버튼 페이지')

# Using "with" notation with st.sidebar:
add_radio = st.radio(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)
st.write(f"당신은\"{add_radio}\"를 선택했습니다.")
st.write("안녕하세요! 이곳은 홈페이지입니다.")