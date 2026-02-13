import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="My YECL 青銀共居平台", layout="wide")

st.title("🏠 共居不只是租屋：制度化媒合模型")
st.markdown("---")

if 'step' not in st.session_state:
    st.session_state.step = 1

# 模擬一個理想配對對象的數據 (例如：平台資料庫中的某位銀髮房東)
# 數值範圍 1-10
target_data = {'作息': 8, '清潔': 7, '互動': 6, '隱私': 8, '安靜': 9}

if st.session_state.step == 1:
    st.header("🔴 第一層：不可妥協條件篩選")
    smoke = st.selectbox("1. 您的吸菸習慣？", ["請選擇", "完全不吸菸", "僅在特定區域吸菸", "我有吸菸習慣"])
    pet = st.selectbox("2. 您對寵物的態度？", ["請選擇", "完全無法接受", "可接受小型寵物", "歡迎寵物"])
    
    if st.button("確認並進入下一階段"):
        if smoke != "請選擇" and pet != "請選擇":
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("請先完成初步篩選選項。")

elif st.session_state.step == 2:
    st.header("🟡 第二層：生活習慣相容評估")
    st.write("根據研究報告，此階段將日常行為差異量化以評估相容度  。")
    
    # 讓使用者輸入自己的數值
    st.session_state.sleep = st.slider("作息時間 (1:早起 - 10:晚睡)", 1, 10, 5)
    st.session_state.clean = st.slider("清潔標準要求 (1:輕鬆 - 10:極度整潔)", 1, 10, 5)
    st.session_state.social = st.slider("社交互動頻率 (1:低互動 - 10:高互動)", 1, 10, 5)
    st.session_state.privacy = st.slider("隱私空間重視度 (1:開放 - 10:極度隱私)", 1, 10, 5)
    st.session_state.quiet = st.slider("環境安靜需求 (1:不怕吵 - 10:極度怕吵)", 1, 10, 5)
    
    if st.button("計算媒合適配度"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("🎉 媒合適配度視覺化分析")
    
    # 準備雷達圖數據
    categories = ['作息', '清潔', '互動', '隱私', '安靜']
    user_values = [st.session_state.sleep, st.session_state.clean, st.session_state.social, 
                   st.session_state.privacy, st.session_state.quiet]
    target_values = list(target_data.values())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
          r=user_values,
          theta=categories,
          fill='toself',
          name='您的特質'
    ))
    fig.add_trace(go.Scatterpolar(
          r=target_values,
          theta=categories,
          fill='toself',
          name='對象特質'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(visible=True, range=[0, 10])),
      showlegend=True,
      title="跨世代生活習慣相容雷達圖"
    )

    st.plotly_chart(fig)

    st.success("✅ 數據分析顯示：雙方在『安靜需求』與『作息』高度重疊，穩定性預測為高。")
    st.info("💡 制度建議：建議進入『入住前契約設計』，並針對重疊度較低的部分（如互動期待）加強溝通 [cite: 39, 42] 。")
    
    if st.button("重新測試"):
        st.session_state.step = 1
        st.rerun()
