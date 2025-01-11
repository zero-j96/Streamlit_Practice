# 탭 생성

import streamlit as st

st.title('나의 머신러닝 프로젝트')

#탭 생성
tab_titles = ['데이터 전처리', '모델 훈련', '모델 평가','결과 시각화']
tabs = st.tabs(tab_titles)

#데이터 전처리 탭에 콘텐츠 추가
with tabs[0]:
    st.header('데이터 전처리')
    st.write('데이터 전처리를 수행할 수 있는 곳 입니다.')

#모델 훈련 탭에 콘텐츠 추가
with tabs[1]:
    st.header('모델 훈련')
    st.write('모델 훈련을 수행할 수 있는 곳 입니다.')

#모델 평가 탭에 콘텐츠 추가
with tabs[2]:
    st.header('모델 평가')
    st.write('모델 평가를 수행할 수 있는 곳 입니다.')

#결과 시각화 탭에 콘텐츠 추가
with tabs[3]:
    st.header('결과 시각화')
    st.write('결과 시각화를 수행할 수 있는 곳 입니다.')