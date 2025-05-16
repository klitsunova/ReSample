import streamlit as st
import pandas as pd

def show_download(df):
    st.header("💾 Сохранение результата")
    if st.button("Скачать сбалансированный датасет"):
        df.to_csv("balanced_dataset.csv", index=False)
        st.success("✅ Файл сохранен!")