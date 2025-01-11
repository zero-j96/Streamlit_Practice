import streamlit as st
import pandas as pd
# ------------- 1. streamlit 설치 ----------------------
# 앱 제목 설정
st.title('첫 번째 Streamlit 앱')
# 텍스트 출력
st.write('안녕하세요! Streamlit입니다.')
st.write('오늘은 스트림릿을 배울거에요.')
# 이미지 출력
st.image('streamlit_logo.png', width=200)
# 데이터 프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]}
df = pd.DataFrame(data)
# 데이터 프레임 출력
st.dataframe(df)
# 막대 그래프 생성
st.bar_chart(df['age'])