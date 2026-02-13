import streamlit as st
import plotly.graph_objects as go

# 1. 頁面配置與佈局優化
st.set_page_config(page_title="致理溫馨共居平台", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    .stButton>button { background-color: #FF8C00; color: white; border-radius: 20px; width: 100%; }
    .stProgress > div > div > div > div { background-color: #32CD32; }
    </style>
    """, unsafe_allow_html=True)

# 2. 側邊欄：身份切換與制度保障
with st.sidebar:
    st.title("👤 角色切換")
    role = st.radio("請選擇您的瀏覽視角：", ["房東長者 (Senior)", "青年房客 (Youth)"])
    st.markdown("---")
    st.title("🛡️ 安全居住保障")
    st.info("""
    本平台由制度模型支撐，旨在透過流程提升共居穩定性：
    1. **三層篩選**：排除基本不合、評估習慣、釐清期待。
    2. **制度支撐**：提供標準公約與契約範本。
    3. **關係維持**：入住後追蹤與第三方協調機制。
    """)

# 初始化進度狀態
if 'step' not in st.session_state:
    st.session_state.step = 1

# 3. 共享邏輯：雷達圖繪製函數
def draw_radar(u_values, t_values, u_name, t_name):
    categories = ['作息規律', '清潔標準', '社交頻率', '隱私需求', '互動期待']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=u_values, theta=categories, fill='toself', name=u_name))
    fig.add_trace(go.Scatterpolar(r=t_values, theta=categories, fill='toself', name=t_name))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=True,
        title=f"生活習慣相容性分析雷達圖"
    )
    return fig

# ==========================================
# 4. 長者房東視角 (完整保留原有功能)
# ==========================================
if role == "房東長者 (Senior)":
    st.title("🏡 致理愛生活：讓空房變溫暖 (房東版)")
    st.write("透過制度化設計，為跨世代共居提供穩定且具安全感的媒合流程。")
    
    st.progress(st.session_state.step / 4.0)

    if st.session_state.step == 1:
        st.subheader("🌸 第一步：生活小堅持 (初步篩選)")
        st.write("排除無法調整的生活條件差異，降低衝突風險。")
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.smoke = st.selectbox("🚬 關於抽菸...", ["請選擇", "我不吸菸", "僅在陽台吸菸", "我有吸菸習慣"])
        with col2:
            st.session_state.pet = st.selectbox("🐾 關於毛小孩...", ["請選擇", "不方便接觸", "可接受小型", "歡迎毛孩"])
        if st.button("下一步：聊聊生活習慣"):
            if st.session_state.smoke != "請選擇": st.session_state.step = 2; st.rerun()

    elif st.session_state.step == 2:
        st.subheader("☀️ 第二步：生活節奏與互動 (相容度評估)")
        sleep_map = {"早睡早起": 9, "一般作息": 6, "晚起族": 3}
        sleep_choice = st.select_slider("🌙 您的作息規律嗎？", options=["早睡早起", "一般作息", "晚起族"])
        st.session_state.sleep_val = sleep_map[sleep_choice]
        st.session_state.clean_val = st.slider("🧹 整潔重視度？", 1, 10, 8)
        st.session_state.social_val = st.slider("☕ 互動頻率？", 1, 10, 5)
        st.session_state.privacy_val = st.slider("🔑 隱私空間重視度？", 1, 10, 8)
        if st.button("下一步：最後的認知確認"): st.session_state.step = 3; st.rerun()

    elif st.session_state.step == 3:
        st.subheader("🤝 第三步：彼此的期待 (角色認知)")
        st.warning("⚠️ 溫馨提醒：本模型強調「非照護、界線清楚的共居互助」。")
        understand = st.checkbox("我已理解這是一份跨世代的互助共居，而非提供或尋求「照護服務」。")
        if st.button("完成！產出媒合分析"):
            if understand: st.session_state.step = 4; st.balloons(); st.rerun()

    elif st.session_state.step == 4:
        st.header("🎉 專屬於您的媒合適配報告")
        radar_fig = draw_radar(
            [st.session_state.get('sleep_val', 5), st.session_state.get('clean_val', 5), 
             st.session_state.get('social_val', 5), st.session_state.get('privacy_val', 5), 7],
            [8, 7, 6, 8, 9], "您的特質", "理想青年"
        )
        st.plotly_chart(radar_fig, use_container_width=True)
        st.success("✅ 建議進入『入住前契約設計』階段。")
        if st.button("重新進行媒合測試"): st.session_state.step = 1; st.rerun()

# ==========================================
# 5. 青年房客視角 (針對青年需求優化)
# ==========================================
elif role == "青年房客 (Youth)":
    st.title("🎓 青年專區：找的不只是房，是成長夥伴")
    st.write("我們重視您的**生活自主性**。提供合約規範且無照護負擔的共居選擇。")
    
    tab_y1, tab_y2, tab_y3 = st.tabs(["🛡️ 居住底線", "🤝 互助自選", "📊 數據報告"])
    
    with tab_y1:
        st.subheader("🔴 第一層：生活小堅持")
        st.info("⚠️ 平台保證：合約標準化，明確聲明非照護義務。")
        y_smoke = st.selectbox("🚬 您的吸菸習慣？", ["我不吸菸", "僅特定區域", "有菸習慣"], key="y_smoke")
        y_pet = st.selectbox("🐾 您有攜帶寵物嗎？", ["無寵物", "有小型寵物", "有大型寵物"], key="y_pet")
        
    with tab_y2:
        st.subheader("🟡 第二層：互助內容與作息")
        st.write("定義您願意提供的生活互助項目（技能交換）：")
        y_help = st.multiselect("我願意提供：", ["3C 產品教學", "順手代丟垃圾", "每週一次共食", "協助代收掛號"], default=["3C 產品教學"])
        y_sleep = st.slider("🌙 您的作息規律 (1:早起 - 10:熬夜族)", 1, 10, 5)
        y_clean = st.slider("🧹 您對環境整潔的要求？", 1, 10, 5)
        st.caption("明確的互助項目能有效降低共居初期的認知落差。")

    with tab_y3:
        st.subheader("🎉 您的適配分析報告")
        # 繪製青年視角的對比雷達圖
        y_radar = draw_radar([y_sleep, y_clean, 7, 7, 8], [8, 8, 5, 8, 6], "青年(您)", "銀髮房東")
        st.plotly_chart(y_radar, use_container_width=True)
        st.success("✅ 找到匹配房東！對方極度歡迎您的『3C 教學』專長。")
        st.info("💡 制度建議：建議下載『數位生活公約』，確保生活邊界明確。")

# 6. 頁尾共用資訊
st.markdown("---")
st.caption("致理愛生活：制度化媒合模型。致力於解決高齡獨居問題，並營造跨世代互助環境。")
