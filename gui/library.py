import streamlit as st

def show_library():
    st.markdown("<h1 class='classic-title'>📚 Disease Library</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4B5563; margin-bottom: 30px;'>Learn about common plant diseases, their symptoms, and how to treat them.</p>", unsafe_allow_html=True)
    
    diseases = [
        {
            "name": "Potato Early Blight",
            "image": "https://images.unsplash.com/photo-1628169828859-e93237190d6e?q=80&w=400&auto=format&fit=crop", # Unsplash image representing diseased leaf
            "symptoms": "Brown or black spots with concentric rings on older leaves.",
            "description": "A common fungal disease that affects the lower leaves first, causing them to yellow and drop off."
        },
        {
            "name": "Potato Late Blight",
            "image": "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=400&auto=format&fit=crop", # Unsplash image
            "symptoms": "Water-soaked spots on leaves that turn dark brown or black. White fuzzy mold on undersides in humid conditions.",
            "description": "A highly destructive fungal disease that spreads rapidly in wet, cool conditions, affecting both leaves and tubers."
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, disease in enumerate(diseases):
        with (col1 if i % 2 == 0 else col2):
            with st.container():
                st.markdown(f'<img src="{disease["image"]}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">', unsafe_allow_html=True)
                st.markdown(f"<h3 style='margin-top: 15px; color: #134021;'>{disease['name']}</h3>", unsafe_allow_html=True)
                st.write(f"**Symptoms:** {disease['symptoms']}")
                st.write(disease["description"])
                st.button(f"Learn More about {disease['name']}", key=f"learn_{i}")
                st.markdown("<hr style='opacity: 0.2; margin: 30px 0;'>", unsafe_allow_html=True)
