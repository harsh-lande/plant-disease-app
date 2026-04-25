import streamlit as st

def show_tips():
    st.header("💡 Plant Care Tips")
    st.markdown("Industry-standard guidelines to keep your plants thriving and disease-free.")
    
    with st.expander("💧 Optimal Watering Techniques", expanded=True):
        st.write("Potatoes need consistent moisture, especially during tuber formation. Water deeply 1-2 inches per week. Avoid overhead watering to keep foliage dry, which prevents Early and Late Blight.")
        
    with st.expander("🌱 Soil & Hilling Management", expanded=True):
        st.write("Plant in loose, well-draining, slightly acidic soil (pH 5.8-6.5). Regularly 'hill' soil around the stems as the plant grows to protect developing tubers from sun exposure (which causes greening) and blight spores.")
        
    with st.expander("🌬️ Air Circulation & Spacing", expanded=True):
        st.write("Space seed potatoes 12-15 inches apart in rows 3 feet apart. Good air circulation is critical for drying leaves quickly after rain or morning dew, significantly reducing fungal disease risks.")
        
    with st.expander("🐛 Potato Pest Management"):
        st.write("Monitor weekly for Colorado Potato Beetles and aphids. Hand-pick beetle larvae or use organic controls like Neem Oil or Spinosad. Aphids can transmit viral diseases, so manage them early.")
        
    with st.expander("☀️ Light Requirements"):
        st.write("Potatoes require full sun (at least 6-8 hours of direct sunlight daily) for optimal growth and high tuber yields.")
        
    with st.expander("🧹 Crop Rotation & Sanitation"):
        st.write("Practice a 3-4 year crop rotation (do not plant potatoes where tomatoes, peppers, or eggplants grew recently). Remove and destroy all plant debris at the end of the season to prevent blight spores from overwintering.")
