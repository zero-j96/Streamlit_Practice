import streamlit as st
st.text('아래의 예제는 함수를 활용한 예제입니다.')

def get_user_name():
    return 'John'

def get_puctuation():
    return '!!!'

greeting = 'Hi there,'
user_name = get_user_name()
punctuation = get_puctuation()

st.write('이 윗 부분의 함수 정의부는 화면에 출력되지 않습니다.')
st.write(greeting, user_name, punctuation)

#...up to here
st.write('Done!')
st.divider()