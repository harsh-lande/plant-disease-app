import bcrypt
import streamlit as st

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def set_logged_in(user_id: int, username: str):
    """Set session state variables for a logged-in user."""
    st.session_state['logged_in'] = True
    st.session_state['user_id'] = user_id
    st.session_state['username'] = username
    st.session_state['page'] = "dashboard"

def logout():
    """Clear session state variables."""
    st.session_state['logged_in'] = False
    st.session_state['user_id'] = None
    st.session_state['username'] = None
    st.session_state['page'] = "landing"
