import streamlit as st
import sqlite3
from database.db import execute_query
from auth.auth_utils import hash_password

def show_register():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("← Back to Landing", key="back_reg"):
            st.session_state['page'] = "landing"
            st.rerun()
            
        st.write("")
        st.header("Create an Account")
        
        with st.form("register_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Sign Up", use_container_width=True)
            
            if submitted:
                if not username or not email or not password:
                    st.error("Please fill in all required fields.")
                elif password != confirm_password:
                    st.error("Passwords do not match.")
                elif len(password) < 6:
                    st.error("Password must be at least 6 characters long.")
                else:
                    hashed_pw = hash_password(password)
                    try:
                        user_id = execute_query(
                            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                            (username, email, hashed_pw)
                        )
                        st.success("Account created successfully! Redirecting to login...")
                        import time
                        time.sleep(1.5)
                        st.session_state['page'] = "login"
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.error("Username or email already exists. Please choose a different one.")
                        
        st.write("Already have an account?")
        if st.button("Log In Here", use_container_width=True):
            st.session_state['page'] = "login"
            st.rerun()
