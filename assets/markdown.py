import streamlit as st

st.set_page_config(page_title="Data Balancer", layout="wide", page_icon="🔄")
st.title("🔄 Synthetic Data Generator")
st.sidebar.subheader("ℹ️ About this App")
st.sidebar.info("""
👋 **Welcome!**  \n\n\n
Effortlessly preprocess and balance your datasets with **SMOTE** for improved model performance.
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
📧 **Contact:** kshethia11@gmail.com  
""")
