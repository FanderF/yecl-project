import streamlit as st
import plotly.graph_objects as go

# 1. 頁面配置與佈局優化 [cite: 112]
st.set_page_config(page_title="My YECL 溫馨共居平台", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    .stButton>button { background-color: #FF8C00; color: white; border-radius: 20px; width: 100%; }
    .stProgress > div > div > div > div { background-color: #32CD32; }
    </style>
    """, unsafe_allow_html=True)

# 2. 側邊欄：制度保障與風險控管說明 [cite: 32, 43]
st.sidebar.title("🛡️ 安全居住保障")
st.sidebar.info("""
本平台由制度模型支撐，旨在透過流程提升共居穩定性 [cite: 9, 30]：
1. **三層篩選**：排除基本不合、評估習慣、釐清期待 [cite: 35]。
2. **制度支撐**：提供標準公約與契約範本 [cite: 42]。
3. **關係維持**：入住後追蹤與第三方協調機制 [cite: 43]。
""")

# 3. 標題與研究引言 [cite: 4]
st.title("🏡 My YECL：共居不只是租屋 [cite: 7]")
st.write("透過制度化設計，為跨世代共居提供穩定且具安全感的媒合流程 。")

# 初始化進度狀態
if 'step' not in st.session_state:
    st.session_state.step = 1

# 進度條顯示 [cite: 48]
progress_map = {1: 0.25, 2: 0.5, 3: 0.75, 4: 1.0}
st.progress(progress_map.get(st.session_state.step, 0.1))

# --- 步驟流程控制 ---

# 第一步：不可妥協條件篩選 (風險前移處理) [cite: 30, 37]
if st.session_state.step == 1:
    st.subheader("🌸 第一步：生活小堅持 (初步篩選) [cite: 37]")
    st.write("排除無法調整的生活條件差異，降低媒合後的高衝突風險 [cite: 17, 37]。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.smoke = st.selectbox("🚬 關於抽菸...", ["請選擇", "我不吸菸", "僅在陽台吸菸", "我有吸菸習慣"])
    with col2:
        st.session_state.pet = st.selectbox("🐾 關於毛小孩...", ["請選擇", "不方便接觸寵物", "可接受小型寵物", "我是毛孩愛愛好者"])
    
    if st.button("下一步：聊聊生活習慣"):
        if st.session_state.smoke != "請選擇" and st.session_state.pet != "請選擇":
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("為了落實篩選制度，請先完成這兩個小選擇喔！ [cite: 37]")

# 第二步：生活習慣相容評估 (量化數據收集) 
elif st.session_state.step == 2:
    st.subheader("☀️ 第二步：生活節奏與互動 (相容度評估) ")
    st.write("透過量化指標，預估入住後的互動品質與相容程度 [cite: 16, 38]。")
    
    # 將滑桿數據存入 session_state 以供雷達圖調用 [cite: 89]
    sleep_map = {"早睡早起": 9, "一般作息": 6, "晚起族": 3}
    sleep_choice = st.select_slider("🌙 您的作息規律嗎？", options=["早睡早起", "一般作息", "晚起族"])
    st.session_state.sleep_val = sleep_map[sleep_choice]
    
    st.session_state.clean_val = st.slider("🧹 您對環境整潔的重視度？(1: 隨興 - 10: 極致整潔)", 1, 10, 5)
    st.session_state.social_val = st.slider("☕ 期待與室友互動的頻率？(1: 偶爾招呼 - 10: 經常共餐)", 1, 10, 5)
    st.session_state.privacy_val = st.slider("🔑 對個人隱私空間的重視度？(1: 開放 - 10: 極度重視)", 1, 10, 5)
    
    if st.button("下一步：最後的認知確認"):
        st.session_state.step = 3
        st.rerun()

# 第三步：角色期待分析 (避免照護認知落差) [cite: 30, 39]
elif st.session_state.step == 3:
    st.subheader("🤝 第三步：彼此的期待 (角色認知) [cite: 39]")
    st.warning("⚠️ 溫馨提醒：本模型強調「非照護、界線清楚的共居互助」 [cite: 30, 66]。")
    
    understand = st.checkbox("我已理解這是一份跨世代的互助共居，而非提供或尋求「照護服務」 [cite: 66, 69]。")
    st.session_state.expect = st.multiselect("您對共居的期待包含？", ["生活安全感", "技能交換", "減少租金負擔", "情感陪伴"])
    
    if st.button("完成！產出媒合適配報告"):
        if understand:
            st.session_state.step = 4
            st.balloons()
            st.rerun()
        else:
            st.error("根據研究發現，角色認知一致是關係穩定的關鍵，請先確認上述聲明 [cite: 30]。")

# 第四步：視覺化分析與制度建議 [cite: 89, 95]
elif st.session_state.step == 4:
    st.header("🎉 專屬於您的媒合適配報告 [cite: 89]")
    st.write("根據您的回覆與系統資料庫比對，量化分析結果如下 [cite: 33, 89]：")
    
    # 準備雷達圖數據 [cite: 89]
    categories = ['作息規律', '清潔標準', '社交頻率', '隱私需求', '互動期待']
    # 抓取第二步儲存的數值，若無則預設為 5
    user_values = [
        st.session_state.get('sleep_val', 5),
        st.session_state.get('clean_val', 5),
        st.session_state.get('social_val', 5),
        st.session_state.get('privacy_val', 5),
        7 # 互動期待固定值模擬
    ]
    # 模擬一位理想對象的數據 [cite: 87]
    target_values = [8, 7, 6, 8, 9]

    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=user_values, theta=categories, fill='toself', name='您的特質'))
    fig.add_trace(go.Scatterpolar(r=target_values, theta=categories, fill='toself', name='理想對象'))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=True,
        title="生活習慣相容性分析雷達圖 [cite: 89]"
    )

    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ 系統顯示：您與潛在對象在『生活規律』與『環境標準』高度契合！ [cite: 89]")
    
    st.markdown("---")
    st.subheader("📜 制度化後續建議 [cite: 107]")
    st.info("""
    1. **入住前**：建議下載系統提供的「數位生活公約」草案，針對互動頻率進行最後確認 [cite: 42, 71]。
    2. **入住後**：系統將自動啟動為期一個月的初期追蹤，提供第三方協調支援 [cite: 43]。
    """)
    
    if st.button("重新進行媒合測試"):
        st.session_state.step = 1
        st.rerun()
