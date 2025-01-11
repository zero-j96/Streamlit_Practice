import streamlit as st
st.write('아래 코드화면에 출력되는 코드입니다!')

def get_user_name():
    return 'John'

with st.echo():
    def get_punctuation():
        return '!!!'

    greeting = 'Hi there,'
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
st.write('코드의 실행결과도 위에 나타나게 됩니다.')
st.divider()

# write와 text 차이
# text는 문자열로 출력, write는 데이터 타입을 그대로 유지

st.text(123)
st.text(True)
st.write({'test':1})