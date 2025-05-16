import streamlit as st

def set_markdown():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.set_page_config(page_title="ReSample", layout="wide", page_icon="🔄")
    st.title("🔄 Synthetic Data Generator")

    st.sidebar.subheader("ℹ️ About this App")
    st.sidebar.info("""
    👋 **Welcome!**  \n\n\n
    Effortlessly preprocess and balance your datasets with various sampling methods for improved model performance.
    \n
    **Why Synthetic Data?**  
    - Bias Reduction  
    - Privacy Protection  
    - Increased Data Volume  
    - Diverse Scenario Generation  
    - Cost-Effective  
    \n
    **Quick Start:**  
    1. Upload your dataset or use the sample.  
    2. Handle missing values.  
    3. Select the target variable for balancing.  
    4. Compare class distributions.  
    5. Download the processed dataset.  

    \n\n \n \n \n\n\n
    📧 **Contact:** kateryna.klitsunova@gmail.com
    """)
