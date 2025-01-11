import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# 한글 폰트 설정 (전역)
plt.rcParams['font.family'] = 'Malgun Gothic'
# 마이너스 폰트 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
# 앱 제목 설정
st.title("첫 번째 Streamlit 앱")
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'Emma'],
        'age': [30, 25, 22, 21],
        'gender': ['Female', 'Male', 'Male', 'Female']}
df = pd.DataFrame(data)
# 데이터 프레임 출력
st.dataframe(df)
# 데이터 프레임 정렬
sorted_df = df.sort_values(by="age")
# 데이터 프레임 집계
average_age = sorted_df["age"].mean()
st.write("")
# 정렬된 데이터 프레임 출력
st.write('정렬된 데이터 프레임')
st.dataframe(sorted_df)
# 평균 연령 출력
# unsafe_allow_html=True HTML을 작성할 수 있게 함
st.write("평균 연령:", round(average_age, 4))
st.markdown(
    f"""
    <h1 style='font-size:32px; color:white;'>
        평균 연령: <span style='color:yellow;'>{round(average_age, 4)}</span>
    </h1>
    """,
    unsafe_allow_html=True
)
# 성별별 연령 분포 그래프
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="gender", y="age", ci=None, palette="Set2")
plt.xlabel("성별")
plt.ylabel("나이")
plt.title("성별별 평균 연령 분포")
st.pyplot(plt)