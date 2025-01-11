import streamlit as st
import pandas as pd
import time
from datetime import datetime

#구간 선택 슬라이더 value는 초기값 설정
st.slider('날짜 슬라이더', min_value= datetime(2024,1,1),
          max_value = datetime(2024,12,31),
          value = (datetime(2024,3,1),datetime(2024,4,1)))

# 파일 업로드 버튼 (업로드 가능)
file = st.file_uploader('파일 선택(csv or excel)',
                        type = ['csv','xls','xlsx'])

# Excel or CSV 확장자를 구분하여 출력하는 경우
if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file) # 파일 읽기
    elif 'xls' in ext:
        df = pd.read_excel(file, engine = 'openpyxl') # 엑셀 로드
    st.dataframe(df) # 출력