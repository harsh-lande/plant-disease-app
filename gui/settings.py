import streamlit as st
from auth.auth_utils import hash_password
from database.db import execute_query

def show_settings():
    st.header("⚙️ Settings")
    
    st.subheader("Profile Information")
    st.info(f"**Username:** {st.session_state['username']}")
    
    st.markdown("---")
    
    st.subheader("Update Password")
    with st.form("update_password_form"):
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        submitted = st.form_submit_button("Update Password")
        
        if submitted:
            if not new_password:
                st.error("Please enter a new password.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            elif len(new_password) < 6:
                st.error("Password must be at least 6 characters long.")
            else:
                hashed_pw = hash_password(new_password)
                execute_query(
                    "UPDATE users SET password_hash = ? WHERE id = ?",
                    (hashed_pw, st.session_state['user_id'])
                )
                st.success("Password updated successfully!")
