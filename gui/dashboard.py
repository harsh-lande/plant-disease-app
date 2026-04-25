import streamlit as st
import pandas as pd
from database.db import fetch_all, execute_query
from model.predictor import PlantPredictor
from auth.auth_utils import logout

from gui.diagnose import show_diagnose
from gui.history import show_history
from gui.tips import show_tips
from gui.settings import show_settings

def show_dashboard():
    # Initialize dashboard tab state if not present
    if 'dashboard_tab' not in st.session_state:
        st.session_state['dashboard_tab'] = 'Dashboard'
        
    # --- SIDEBAR ---
    with st.sidebar:
        st.subheader("🌿 PlantCare")
        st.write(f"Logged in as: **{st.session_state.get('username', 'User')}**")
        st.divider()
        
        # Navigation buttons
        if st.button("🏠 Dashboard", use_container_width=True, type="primary" if st.session_state['dashboard_tab'] == 'Dashboard' else "secondary"):
            st.session_state['dashboard_tab'] = 'Dashboard'
            st.rerun()
            
        if st.button("📸 Upload Image", use_container_width=True, type="primary" if st.session_state['dashboard_tab'] == 'Upload Image' else "secondary"):
            st.session_state['dashboard_tab'] = 'Upload Image'
            st.rerun()
            
        if st.button("🕰️ History", use_container_width=True, type="primary" if st.session_state['dashboard_tab'] == 'History' else "secondary"):
            st.session_state['dashboard_tab'] = 'History'
            st.rerun()
            
        if st.button("💡 Tips", use_container_width=True, type="primary" if st.session_state['dashboard_tab'] == 'Tips' else "secondary"):
            st.session_state['dashboard_tab'] = 'Tips'
            st.rerun()
            
        if st.button("⚙️ Settings", use_container_width=True, type="primary" if st.session_state['dashboard_tab'] == 'Settings' else "secondary"):
            st.session_state['dashboard_tab'] = 'Settings'
            st.rerun()
            
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()

    # --- MAIN CONTENT ROUTING ---
    tab = st.session_state['dashboard_tab']
    
    if tab == 'Upload Image':
        show_diagnose()
    elif tab == 'History':
        show_history()
    elif tab == 'Tips':
        show_tips()
    elif tab == 'Settings':
        show_settings()
    else:
        # Default Dashboard View (Combined Overview)
        st.markdown(f'''
            <div style="background-image: linear-gradient(rgba(52, 168, 83, 0.8), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'); background-size: cover; background-position: center; border-radius: 15px; padding: 40px 20px; text-align: center; margin-bottom: 25px;">
                <h1 style="color: white; font-size: 2.5rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">Welcome back, {st.session_state.get('username', 'User')} 🌱</h1>
                <p style="color: #F3F4F6; font-size: 1.1rem; margin-top: 10px; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Identify plant diseases fast and get smart solutions to keep your plants healthy.</p>
            </div>
        ''', unsafe_allow_html=True)

        # --- UPLOAD & DETECTION SECTION ---
        st.header("📸 Diagnose Your Plant")
        st.write("Upload a leaf image to detect diseases instantly.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], key="dash_uploader")
            if uploaded_file is not None:
                st.image(uploaded_file, caption="Uploaded Leaf", use_column_width=True)

        with col2:
            if uploaded_file is not None:
                if st.button("Analyze Image", type="primary", use_container_width=True, key="dash_analyze"):
                    with st.spinner("Analyzing plant leaf..."):
                        predictor = PlantPredictor()
                        disease, confidence = predictor.predict(uploaded_file)
                        
                        # Determine Severity
                        if disease == "Healthy":
                            severity = "Healthy"
                            st.success(f"**Result:** {disease}")
                            st.write(f"Confidence: {confidence}%")
                        else:
                            if confidence > 90:
                                severity = "Severe"
                            elif confidence > 70:
                                severity = "Moderate"
                            else:
                                severity = "Mild"
                            st.error(f"**Result:** {disease}")
                            st.warning(f"Severity: {severity} | Confidence: {confidence}%")
                            st.info("Tip: Remove affected leaves and apply recommended treatments.")
                        
                        # Save to history
                        if 'user_id' in st.session_state and st.session_state['user_id']:
                            execute_query(
                                "INSERT INTO history (user_id, plant_name, disease, severity) VALUES (?, ?, ?, ?)",
                                (st.session_state['user_id'], "Unknown Plant", disease, severity)
                            )
                            st.success("Diagnosis saved to your History.")
            else:
                st.info("Please upload an image to begin detection.")

        st.divider()

        # --- HISTORY SECTION ---
        st.header("🕰️ Your Detection History")
        
        if 'user_id' in st.session_state and st.session_state['user_id']:
            user_id = st.session_state['user_id']
            # Only fetch last 5 for overview
            records = fetch_all("SELECT plant_name, disease, severity, timestamp FROM history WHERE user_id = ? ORDER BY timestamp DESC LIMIT 5", (user_id,))
            
            if not records:
                st.info("No history found. Diagnose a plant to see records here.")
            else:
                df = pd.DataFrame(records, columns=["Plant", "Disease", "Severity", "Date & Time"])
                st.dataframe(df, use_container_width=True, hide_index=True)
                if st.button("View Full History", key="dash_view_history"):
                    st.session_state['dashboard_tab'] = 'History'
                    st.rerun()
        else:
            st.error("Error loading user history.")
