import streamlit as st
import pandas as pd
from database.db import fetch_all

def show_history():
    st.header("🕰️ Diagnosis History")
    
    user_id = st.session_state['user_id']
    records = fetch_all("SELECT plant_name, disease, severity, timestamp FROM history WHERE user_id = ? ORDER BY timestamp DESC", (user_id,))
    
    if not records:
        st.info("No history found. Diagnose a plant to see records here.")
    else:
        # Convert to DataFrame for nice table display
        df = pd.DataFrame(records, columns=["Plant Name", "Disease", "Severity", "Date & Time"])
        st.dataframe(df, use_container_width=True, hide_index=True)
