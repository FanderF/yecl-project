import streamlit as st
import pandas as pd

# 頁面配置
st.set_page_config(page_title="My YECL 青銀共居平台", layout="wide")

st.title("🏠 共居不只是租屋：制度化媒合模型")
st.markdown("---")

# 側邊欄：研究重點導覽
st.sidebar.header("研究核心理念")
st.sidebar.info("透過制度設計降低風險、維持關係穩定 ")
st.sidebar.markdown("""
- **第一層**：不可妥協條件篩選 [cite: 37]
- **第二層**：生活習慣相容評估 [cite: 38]
- **第三層**：角色期待認知分析 [cite: 39]
""")

# 初始化 Session State
if 'step' not in st.session_state:
    st.session_state.step = 1

# 流程控制
if st.session_state.step == 1:
    st.header("🔴 第一層：不可妥協條件篩選")
    st.write("本階段旨在排除無法調整的生活條件差異，降低衝突風險 [cite: 37] 。")
    
    col1, col2 = st.columns(2)
    with col1:
        smoke = st.selectbox("1. 您的吸菸習慣？", ["請選擇", "完全不吸菸", "僅在特定區域吸菸", "我有吸菸習慣"])
    with col2:
        pet = st.selectbox("2. 您對寵物的態度？", ["請選擇", "完全無法接受", "可接受小型寵物", "歡迎寵物"])
    
    if st.button("確認並進入下一階段"):
        if smoke != "請選擇" and pet != "請選擇":
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("請先完成初步篩選選項。")

elif st.session_state.step == 2:
    st.header("🟡 第二層：生活習慣相容評估")
    st.write("針對日常生活細節進行評估，計算相容程度作為媒合依據 [cite: 38] 。")
    
    sleep = st.select_slider("您的作息時間？", options=["早睡早起", "一般作息", "晚睡晚起"])
    clean = st.slider("清潔標準要求 (1: 隨興 - 10: 極度整潔)", 1, 10, 5)
    
    if st.button("下一步：釐清角色期待"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("🔵 第三層：共居期待與角色認知分析")
    st.write("聚焦於雙方對共居關係之理解，降低認知落差 [cite: 39] 。")
    
    st.warning("⚠️ 重要：青銀共居非照護關係，應維持生活自主性 [cite: 30] 。")
    understand = st.checkbox("我已理解這不是「照護」或「服務交換」關係。")
    
    if st.button("產出媒合建議"):
        if understand:
            st.balloons()
            st.success("🎉 媒合適配度計算完成！")
            st.markdown("### 📋 系統分析建議：建議進入入住前契約與生活公約設計階段 [cite: 42] 。")
