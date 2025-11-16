import streamlit as st
import pandas as pd
import time
from datetime import datetime
import os

# Current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')  # ✅ Same format as test.py
timestamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')

st.title("📋 Face Attendance System")

# File path
file_path = f"Attendance/Attendance_{date}.csv"

# Check if file exists
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.success(f"Attendance for {date} loaded successfully ✅")
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.warning(f"No attendance file found for today ({date}). Please run test.py first.")


