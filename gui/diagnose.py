import streamlit as st
import time
from database.db import execute_query
from model.predictor import PlantPredictor

def show_diagnose():
    st.header("📸 Diagnose Your Plant")
    st.markdown("Upload or capture a clear image of the affected plant leaf.")
    
    uploaded_file = st.file_uploader("Drag and drop your image here", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width=300)
        
        if st.button("Analyze Image"):
            with st.spinner("Analyzing plant leaf..."):
                predictor = PlantPredictor()
                disease, confidence = predictor.predict(uploaded_file)
                
                # Determine Severity
                if disease == "Healthy":
                    severity = "Healthy"
                    st.success(f"**Prediction:** {disease} ({confidence}%)")
                else:
                    if confidence > 90:
                        severity = "Severe"
                    elif confidence > 70:
                        severity = "Moderate"
                    else:
                        severity = "Mild"
                    st.error(f"**Prediction:** {disease} ({confidence}%) - {severity}")
                
                # Save to history
                execute_query(
                    "INSERT INTO history (user_id, plant_name, disease, severity) VALUES (?, ?, ?, ?)",
                    (st.session_state['user_id'], "Unknown Plant", disease, severity)
                )
                
                st.info("Diagnosis saved to your History.")
