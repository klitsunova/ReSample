import streamlit as st
import pandas as pd

def load_data(file_path):
    file_extension = file_path.split(".")[-1]
    if file_extension == "csv":
        return pd.read_csv(file_path)
    elif file_extension == "xlsx":
        return pd.read_excel(file_path)
    else:
        raise ValueError("Формат файла не поддерживается")

def show_upload():
    st.header("📂 Загрузка датасета")
    uploaded_file = st.file_uploader("Загрузите файл (.csv, .xlsx)", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        with st.spinner("⏳ Загружаем данные..."):
            df = load_data(uploaded_file.name)
            st.success("✅ Данные загружены!")
            st.dataframe(df.head())
