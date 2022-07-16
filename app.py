import pandas as pd
import streamlit as st

menu = ['질문','정보']
choice = st.sidebar.selectbox('메뉴',menu)

if choice == '질문':

    st.header('설문조사')

    Uname = st.text_input('이름',max_chars=4)
    if len(Uname) <= 0:
        st.error('이름은 최소 한글자 이상이여야 합니다.')

    Uage = st.number_input('나이',min_value=1,max_value=100)

    U_gender = st.radio('성별',
                        ('남', '여'))

    Umail = st.text_area('G-mail 주소',value='xxxxx@gmail.com')

if choice == '정보':
    st.header('답')
    st.write(pd.DataFrame({
        '문항': [1, 2, 3],
        '답': [2, 5, 5]
    }))


