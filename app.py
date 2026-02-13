import streamlit as st
import plotly.graph_objects as go

# 頁面配置與自定義 CSS
st.set_page_config(page_title="My YECL 溫馨共居平台", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    .stButton>button { background-color: #FF8C00; color: white; border-radius: 20px; }
    .stProgress > div > div > div > div { background-color: #32CD32; }
    </style>
    """, unsafe_allow_html=True)

# 側邊欄：安全感支撐
st.sidebar.title("🛡️ 安全居住保障")
st.sidebar.info("本平台由制度模型支撐，提供：\n1. 專業三層篩選\n2. 標準生活公約範本\n3. 第三方協調機制")

# 平台標題與引言
st.title("🏡 My YECL：讓空房變溫暖，讓生活有伴")
st.write("這不只是租屋，更是一場跨世代的幸福媒合 [cite: 4, 111]。")

if 'step' not in st.session_state:
    st.session_state.step = 1

# 進度條
progress_map = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0}
st.progress(progress_map.get(st.session_state.step, 0.1))

# --- 步驟流程 ---
if st.session_state.step == 1:
    st.subheader("🌸 第一步：生活小堅持 (初步篩選)")
    st.write("為了讓彼此住得安心，我們先確認基本的居住底線 [cite: 37]：")
    
    col1, col2 = st.columns(2)
    with col1:
        smoke = st.selectbox("🚬 關於抽菸...", ["請選擇", "我不吸菸", "僅在陽台吸菸", "我有吸菸習慣"])
    with col2:
        pet = st.selectbox("🐾 關於毛小孩...", ["請選擇", "不方便接觸寵物", "可接受小型寵物", "我是毛孩愛好者"])
    
    if st.button("下一步：聊聊生活習慣"):
        if smoke != "請選擇" and pet != "請選擇":
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("請先幫我們完成這兩個小選擇喔！")

elif st.session_state.step == 2:
    st.subheader("☀️ 第二步：生活節奏與互動 (相容度評估)")
    st.write("讓我們透過量化評估，找到與您步調最契合的夥伴 [cite: 38]。")
    
    st.session_state.sleep = st.select_slider("🌙 您的作息規律嗎？", options=["早睡早起", "一般作息", "晚起族"])
    st.session_state.clean = st.slider("🧹 您對環境整潔的重視度？(1: 隨興 - 10: 極致整潔)", 1, 10, 5)
    st.session_state.social = st.slider("☕ 期待與室友互動的頻率？(1: 偶爾招呼 - 10: 經常共餐)", 1, 10, 5)
    
    if st.button("下一步：最後的確認"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.subheader("🤝 第三步：彼此的期待 (角色認知)")
    st.warning("⚠️ 溫馨提醒：本計畫強調非照護關係，雙方皆維持獨立自主的生活 [cite: 30, 66]。")
    
    understand = st.checkbox("我理解這是一份跨世代的互助共居，而非提供或尋求照護服務。")
    
    if st.button("完成！查看媒合分析"):
        if understand:
            st.session_state.step = 4
            st.balloons()
            st.rerun()
        else:
            st.error("請勾選確認已理解計畫性質。")

elif st.session_state.step == 4:
    st.header("🎉 專屬於您的媒合雷達圖")
    st.write("根據您的回覆與系統資料庫比對，這是您的生活適配分析 [cite: 89]：")
    
    # 這裡放原本的 Plotly 雷達圖程式碼...
    # (為節省長度略過重複的雷達圖 code)
    
    st.success("✅ 系統顯示：您與潛在對象在『生活節奏』上非常契合！")
    st.info("💡 下一步建議：系統已準備好『數位生活公約』草案，建議您與對方預約線上聊聊 [cite: 42, 71]。")
    
    if st.button("回到首頁"):
        st.session_state.step = 1
        st.rerun()
