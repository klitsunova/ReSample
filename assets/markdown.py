import streamlit as st

def set_markdown():
    st.markdown(
        """
        <style>
        body {
            background-color: #f4f4f4;
            color: #333;
        }
        .stApp {
            max-width: 100%;  /* Increase width */
            margin: auto;
        }
        .css-18e3th9 {
            padding: 2rem 8rem; /* Increase left and right padding */
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border: none;
            cursor: pointer;
            border-radius: 8px;
        }
        .stSelectbox, .stRadio, .stDataFrame, .stTextInput {
            font-size: 16px;
        }
        .h1 {
            font-size:35px; 
            font-weight: bold; 
            display: flex; 
            align-items: center;
        }
        .h3 {
            font-size:16px;
        }
        .button {
            background-color:#4CAF50; 
            color:white; 
            padding:10px 24px; 
            border:none; 
            border-radius:8px; 
            cursor:pointer;
        }
        .div {
            text-align: center;
        }
        </style>
        """,
    unsafe_allow_html=True
    )

    st.markdown("<h1>🔄 ReSample: Fix Imbalanced Data</h1>", unsafe_allow_html=True)

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
