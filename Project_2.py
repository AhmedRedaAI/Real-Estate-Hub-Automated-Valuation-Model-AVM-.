import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Marketing Intelligence", layout="wide")

# Custom Clean CSS
st.markdown("""
    <style>
    .main { background-color: #0b0f19; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    div[data-testid="stDataFrame"] { background-color: #111827; border-radius: 12px; padding: 10px; border: 1px solid #1f2937; }
    .highlight-box { background-color: #1e293b; padding: 20px; border-radius: 12px; border-left: 4px solid #3b82f6; }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Digital Marketing Acquisition Intelligence")
st.markdown("Cross-channel ad performance, ROI mapping, and efficiency metrics.")

# Load Data
df = pd.read_excel('marketing_data.xlsx')
df['CPC'] = df['Spend'] / df['Clicks']
df['ROI (%)'] = ((df['Revenue'] - df['Spend']) / df['Spend']) * 100

st.subheader("📊 Omni-Channel Performance Matrix")
st.dataframe(
    df.style.format({'Spend': '${:,.2f}', 'Revenue': '${:,.2f}', 'CPC': '${:,.2f}', 'ROI (%)': '{:.2f}%'}),
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Return on Investment (ROI) by Channel")
    fig_roi = px.bar(df, x='Platform', y='ROI (%)', color='ROI (%)', 
                     color_continuous_scale='Blugrn', text_auto='.1f', template='plotly_dark')
    fig_roi.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_roi, use_container_width=True)

with col2:
    st.subheader("🛍️ Budget Spend vs. Generated Revenue")
    fig_comp = px.bar(df, x='Platform', y=['Spend', 'Revenue'], barmode='group',
                      color_discrete_sequence=['#ef4444', '#10b981'], template='plotly_dark')
    fig_comp.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_comp, use_container_width=True)

# Smart Alert
best_platform = df.loc[df['Revenue'].idxmax()]['Platform']
st.markdown(f"""
<div class="highlight-box">
    <h4 style="margin:0; color:#3b82f6;">🚀 Top Performer Insight</h4>
    <p style="margin:5px 0 0 0; color:#94a3b8;">The platform driving the absolute highest volume of gross conversion revenue is <strong>{best_platform}</strong>.</p>
</div>
""", unsafe_allow_html=True)