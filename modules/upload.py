import streamlit as st
import pandas as pd
import time

def upload_new_dataset():
    uploaded_file = st.file_uploader("📂 Upload your dataset (.csv or .xlsx)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]

        with st.spinner("⏳ Loading dataset..."):
            time.sleep(1)
            if file_extension == "csv":
                df = pd.read_csv(uploaded_file)
            elif file_extension == "xlsx":
                df = pd.read_excel(uploaded_file)

        if df.select_dtypes(include=['object']).shape[1] > 0:
            st.error("❌ The uploaded dataset contains non-numeric values. Please upload a dataset with numerical features only.")
            df = None
        return df
    else:
        return None

def upload_sample_dataset():
    sample_data_path = "assets/sample_imbalanced_data_missing_data.csv"
    with st.spinner("⏳ Loading sample dataset..."):
        time.sleep(1)
        df = pd.read_csv(sample_data_path)
        st.success("✅ Using sample dataset.")
    return df


def upload_dataset():
    data_option = st.radio("Choose dataset option:", ["Use Sample Data", "Upload New Data"], horizontal=True)
    if data_option == "Upload New Data":
        df = upload_new_dataset()
    else:
        df = upload_sample_dataset()
    return df


