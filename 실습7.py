import streamlit as st
import pandas as pd
import time
from datetime import datetime
# 슬라이더 생성
age_range = (18, 65)
selected_age = st.slider("나이 선택:", age_range[0], age_range[1])
# 선택된 값 출력
st.write("선택된 나이:", selected_age)
# 데이터 불러오기
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 22]}
df = pd.DataFrame(data)
# 조건부 실행
if  selected_age in df["age"].values:
    st.dataframe(df[df['age']==selected_age])
else:
    st.write(f"{selected_age}살에 대한 데이터는 존재하지 않습니다.")
st.divider()