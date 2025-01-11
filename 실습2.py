

import streamlit as st
import pandas as pd

st.title('데이터프레임 튜토리얼')

#DF 생성
data = {
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
}

df=pd.DataFrame(data)

#DataFrame
#use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용(True/False)
#컨테이너: 화면의 일정 영역 -> 웹 브라우저 화면을 컨테이너로 사용 -> 텍스트, df,차트 등이 화면의 크기에 맞춤
st.dataframe(df,use_container_width=True)

#테이블
#DF와 달리 interactive한 UI를 제공하지 않음
st.table(df)

#메트릭
#지표나 수치를 간단하고 직관적으로 표시 가능
#주로 대시보드나 핵심 성과 지표(KPI)를 시각적으로 표현할 때 사용
st.metric(label ='온도', value ='10℃', delta = '1.2℃')
st.metric(label ='삼성전자', value ='61,000원', delta = '-1,200원')
st.metric(label ='현재 사용자', value ='2,500')
st.write("") # 공백 추가

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label ='달러USD', value ='1,228 원', delta = '-12.00원')
col2.metric(label ='일본JYP(100엔)', value ='958.63원', delta = '-7.44원')
col3.metric(label ='유럽연합EUR', value ='1,335.82원', delta = '11.44원')