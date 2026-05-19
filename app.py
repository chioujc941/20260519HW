import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("Jessie 行事曆網頁")
    st.radio("選擇群組", ["工作", "家庭", "朋友"])

col_left, col_right = st.columns([1, 3], gap="large")

with col_left:
    with st.container(border=True): 
                
        title = st.text_input(
                  "待辦事項",
                  placeholder="請填寫待辦事項名稱..."
                )
        st.button("新增")
        
        today = st.date_input(
                  "選擇日期",
                  datetime.date.today()
                )
        meeting_time = st.time_input(
                          "選擇時間"
                        )
        my_color = st.color_picker(
                     "挑選辨識顏色",
                     "#1A73E8"
                    )
        view = st.segmented_control(
              "檢視模式",
              ["月視角", "週視角"],
              default="月視角"
            )
    
        tag = st.pills(
              "行程屬性",
              ["#工作", "#家庭", "#緊急"]
            )
    
        mins = st.number_input(
             "行程開始前幾分鐘提醒？",
             min_value=0, max_value=60,
             value=15
            )
        

with col_right: 
    st.write("檢視區") 
    tab1, tab2 = st.tabs(["本月重點", "已完成事項"])
    with tab1:
        with st.container(border=True):
            st.header("本月重點") 
            st.write("內容")
    with tab2: 
        st.header("已完成事項") 
        st.line_chart([1, 5, 2, 6, 2, 1])

st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")
    
st.button("按鈕 A")
st.write("")  # 塞入一行空白間距
st.button("按鈕 B")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")
