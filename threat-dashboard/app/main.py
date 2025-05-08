import streamlit as st
import pandas as pd
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("/app/logs/logs.jsonl")

st.set_page_config(page_title="Threat Dashboard", layout="wide")
st.title("🛡️ AI Threat Defense Dashboard")

@st.cache_data(ttl=5)
def load_logs():
    if not LOG_FILE.exists():
        return pd.DataFrame()
    lines = LOG_FILE.read_text().strip().split("\n")
    records = [json.loads(line) for line in lines if line]
    df = pd.DataFrame(records)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df.sort_values("timestamp", ascending=False)

df = load_logs()

if df.empty:
    st.warning("No logs found.")
else:
    st.metric("Total Logs", len(df))
    st.metric("Threats Detected", df["input_threat_detected"].sum() + df["output_threat_detected"].sum())

    # Filters
    st.sidebar.title("Filters")
    user_filter = st.sidebar.multiselect("User ID", df["user_id"].unique())
    if user_filter:
        df = df[df["user_id"].isin(user_filter)]

    threat_only = st.sidebar.checkbox("Only show threats", value=False)
    if threat_only:
        df = df[(df["input_threat_detected"]) | (df["output_threat_detected"])]

    st.dataframe(df, use_container_width=True)
