import streamlit as st
import pandas as pd
import numpy as np

st.title('DEMO')
st.write('HAHA')
st.text("Fixed width text")
a = 100
st.write(a)

b = np.array([10,20,30,40,50])
st.write(b)

c = pd.DataFrame({'name':['joe','jack','mary'], 'age':[17,22,18]})
st.write(c)

#核取方塊
st.write('核取方塊')
c1 = st.checkbox("是否加點飲料?")
if c1:#打勾, True
    st.info("要加點飲料")
else:
    st.warning("不加點飲料")

#按鈕
st.write('按鈕')
def show():
    st.write("123467898794251")
btn = st.button("確認")
if btn:#按下按鈕代表True
    show()


