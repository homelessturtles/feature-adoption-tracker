import streamlit as st
import pandas as pd
from analyzer import analyze_logs
from summarizer import summarize_usage

st.set_page_config(page_title="Feature Adoption Tracker")
st.title("📊 Feature Adoption Tracker")

# Upload CSV
uploaded_file = st.file_uploader("Upload your product log CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📁 Raw Logs")
    st.dataframe(df.head())

    st.subheader("📈 Feature Usage Summary")
    usage_stats = analyze_logs(df)
    st.bar_chart(usage_stats)

    st.subheader("🧠 GPT Summary")
    if st.button("Generate Summary"):
        summary = summarize_usage(usage_stats)
        st.success(summary)
else:
    st.info("Upload a CSV file with columns: user_id, event_name, feature, timestamp")