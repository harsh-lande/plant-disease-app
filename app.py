import streamlit as st
import os

# Initialize database
from database.db import init_db
init_db()

# Page configuration
st.set_page_config(
    page_title="PlantCare",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Removed load_css to prevent rendering issues and white-on-white text

# Import Views
from auth.landing import show_landing_page
from auth.login import show_login
from auth.register import show_register
from gui.dashboard import show_dashboard

# STATE MANAGEMENT
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'page' not in st.session_state:
    st.session_state['page'] = "landing"

# APP FLOW / ROUTING
if not st.session_state['logged_in']:
    if st.session_state['page'] == "landing":
        show_landing_page()
    elif st.session_state['page'] == "login":
        show_login()
    elif st.session_state['page'] == "register":
        show_register()
    else:
        st.session_state['page'] = "landing"
        st.rerun()
else:
    # Always show dashboard if logged in
    st.session_state['page'] = "dashboard"
    show_dashboard()
