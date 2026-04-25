import streamlit as st
from database.db import fetch_one
from auth.auth_utils import verify_password, set_logged_in

def show_login():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("← Back to Landing", key="back_login"):
            st.session_state['page'] = "landing"
            st.rerun()
            
        st.write("")
        st.header("Welcome Back")
        
        with st.form("login_form"):
            username_or_email = st.text_input("Username or Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log In", use_container_width=True)
            
            if submitted:
                if not username_or_email or not password:
                    st.error("Please fill in all fields.")
                else:
                    user = fetch_one("SELECT * FROM users WHERE username = ? OR email = ?", (username_or_email, username_or_email))
                    if user and verify_password(password, user['password_hash']):
                        set_logged_in(user['id'], user['username'])
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")
                        
        st.write("Don't have an account?")
        if st.button("Register Here", use_container_width=True):
            st.session_state['page'] = "register"
            st.rerun()
