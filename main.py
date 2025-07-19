# 首頁:分側邊欄與主視窗
import streamlit as st

ps = st.navigation([
    #第一頁
    st.Page("pages/p1.py",title="IRIS樣本資訊",icon='🌷'),
    #第二頁
    st.Page("pages/p2.py",title="IRIS品種預測",icon='👌')
])
ps.run()  # 啟動導覽功能
