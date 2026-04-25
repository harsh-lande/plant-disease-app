import streamlit as st

def show_landing_page():
    # --- NAVBAR ---
    nav_left, nav_mid, nav_right1, nav_right2 = st.columns([1, 4, 1, 1])
    with nav_left:
        st.subheader("🌿 PlantCare")
    with nav_mid:
        st.write("Home &nbsp; | &nbsp; Features &nbsp; | &nbsp; How It Works &nbsp; | &nbsp; About Us &nbsp; | &nbsp; Contact")
    with nav_right1:
        if st.button("Login", use_container_width=True):
            st.session_state['page'] = "login"
            st.rerun()
    with nav_right2:
        if st.button("Register", type="primary", use_container_width=True):
            st.session_state['page'] = "register"
            st.rerun()

    st.divider()

    # --- HERO SECTION ---
    hero_left, hero_right = st.columns([1.2, 1])
    
    with hero_left:
        st.info("🍃 Smart Plant Care, Healthy Future")
        st.title("Detect. Diagnose. Protect Your Plants.")
        st.write("Upload a leaf image and our AI system detects diseases, provides solutions, and helps your plants stay healthy.")
        
        btn_col1, btn_col2, _ = st.columns([1, 1, 2])
        with btn_col1:
            if st.button("Login", type="primary", use_container_width=True, key="hero_login"):
                st.session_state['page'] = "login"
                st.rerun()
        with btn_col2:
            if st.button("Register", use_container_width=True, key="hero_register"):
                st.session_state['page'] = "register"
                st.rerun()
                
        st.write("")
        st.write("")
        
        # Highlights
        h1, h2, h3 = st.columns(3)
        with h1:
            st.success("⚙️ AI Powered\n\nAccurate Detection")
        with h2:
            st.success("🛡️ Instant Results\n\nQuick Diagnosis")
        with h3:
            st.success("🌱 Expert Solutions\n\nBest Remedies")

    with hero_right:
        st.image("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="Smart Plant Detection", use_column_width=True)

    st.divider()
    
    # --- FEATURES SECTION ---
    st.markdown("<center><h3>Everything You Need for Plant Care</h3><p>Powerful tools to detect, diagnose and treat plant diseases effectively.</p></center>", unsafe_allow_html=True)
    st.write("")
    
    f1, f2, f3, f4, f5 = st.columns(5)
    with f1:
        st.info("📸 **Disease Detection**\n\nUpload leaf images and get accurate disease detection using AI.")
    with f2:
        st.info("📄 **Detailed Information**\n\nGet comprehensive information about the disease, symptoms and causes.")
    with f3:
        st.info("🌱 **Treatment Solutions**\n\nReceive effective treatment recommendations and organic control methods.")
    with f4:
        st.info("📊 **Care Tips**\n\nGet personalized plant care tips and best practices for healthy plants.")
    with f5:
        st.info("🕰️ **History Tracking**\n\nTrack your past detections and monitor plant health over time.")
