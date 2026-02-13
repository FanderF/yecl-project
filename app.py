import streamlit as st
import plotly.graph_objects as go

# 1. 頁面配置與佈局
st.set_page_config(page_title="致理溫馨共居平台", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #FFFAF0; }
    .stButton>button { background-color: #FF8C00; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 側邊欄：身份切換
with st.sidebar:
    st.title("👤 角色切換")
    role = st.radio("請選擇您的瀏覽視角：", ["房東長者 (Senior)", "青年房客 (Youth)"])
    st.markdown("---")
    st.info("🛡️ 安全保障：本平台提供法律租賃契約保障與非照護義務聲明。")

# 3. 共享繪圖函數
def draw_radar(u_values, t_values, u_name, t_name):
    categories = ['作息規律', '清潔標準', '社交頻率', '隱私需求', '互動期待']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=u_values, theta=categories, fill='toself', name=u_name))
    fig.add_trace(go.Scatterpolar(r=t_values, theta=categories, fill='toself', name=t_name))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True)
    return fig

# ==========================================
# 4. 長者房東視角 (保留原有完整功能)
# ==========================================
if role == "房東長者 (Senior)":
    st.title("🏡 致理愛生活：房東專區")
    step_s = st.radio("目前進度：", ["生活堅持", "相容評估", "分析報告"], horizontal=True)
    
    if step_s == "生活堅持":
        st.subheader("🌸 第一步：初步篩選")
        s_smoke = st.selectbox("🚬 關於抽菸...", ["我不吸菸", "僅特定區域", "有菸習慣"])
        s_pet = st.selectbox("🐾 關於毛小孩...", ["不方便接觸", "可接受小型", "歡迎毛孩"])
        
    elif step_s == "相容評估":
        st.subheader("☀️ 第二步：生活節奏")
        s_sleep = st.slider("🌙 您的作息規律 (1:早起 - 10:晚起)", 1, 10, 8)
        s_clean = st.slider("🧹 環境整潔重視度", 1, 10, 8)
        st.session_state.s_data = [s_sleep, s_clean, 5, 8, 7]
        
    elif step_s == "分析報告":
        st.subheader("🎉 媒合分析")
        data = st.session_state.get('s_data', [8, 8, 5, 8, 7])
        st.plotly_chart(draw_radar(data, [6, 5, 7, 7, 8], "房東(您)", "匹配青年"))

# ==========================================
# 5. 青年房客視角 (修復滑桿互動功能)
# ==========================================
elif role == "青年房客 (Youth)":
    st.title("🎓 青年專區：找的不只是房，是成長夥伴")
    st.write("我們重視您的**生活自主性**。提供合約規範且無照護負擔的共居選擇。")
    
    tab1, tab2, tab3 = st.tabs(["🛡️ 居住底線", "🤝 互助自選", "📊 數據報告"])
    
    with tab1:
        st.subheader("🔴 第一層：生活小堅持")
        y_smoke = st.selectbox("🚬 您的吸菸習慣？", ["我不吸菸", "僅特定區域", "有菸習慣"], key="y_smoke_act")
        y_pet = st.selectbox("🐾 您有攜帶寵物嗎？", ["無寵物", "有小型寵物", "有大型寵物"], key="y_pet_act")
        
    with tab2:
        st.subheader("🟡 第二層：互助內容與作息")
        st.write("定義您願意提供的生活互助項目：")
        y_help = st.multiselect("我願意提供：", ["3C 產品教學", "順手代丟垃圾", "每週一次共食", "協助代收掛號"], default=["3C 產品教學"])
        
        # 修正後的互動滑桿
        y_sleep = st.slider("🌙 您的作息規律 (1:早起 - 10:熬夜族)", 1, 10, 7, key="y_sleep_slider")
        y_clean = st.slider("🧹 您對環境整潔的要求？(1:隨興 - 10:極致)", 1, 10, 8, key="y_clean_slider")
        
        # 將數據存入 session_state
        st.session_state.y_data = [y_sleep, y_clean, 7, 7, 8]
        st.caption("💡 拖動滑桿即可調整您的數值，這些數據將反映在最後的分析圖中。")

    with tab3:
        st.subheader("🎉 您的適配分析報告")
        y_vals = st.session_state.get('y_data', [7, 8, 7, 7, 8])
        st.plotly_chart(draw_radar(y_vals, [8, 8, 5, 8, 6], "青年(您)", "銀髮房東"), use_container_width=True)
        st.success("✅ 數據已即時更新！您與房東的特質重疊度顯示於圖表中。")

st.markdown("---")
st.caption("致理愛生活：制度化媒合模型。致力於解決高齡獨居問題。")
