import streamlit as st
import pandas as pd

def handle_missing_values(df, strategy="mean"):
    if strategy == "drop":
        return df.dropna()
    elif strategy == "mean":
        return df.fillna(df.mean())
    elif strategy == "median":
        return df.fillna(df.median())
    elif strategy == "mode":
        return df.fillna(df.mode().iloc[0])
    else:
        return df

def show_preprocessing_options():
    st.header("🧹 Предобработка данных")
    missing_strategy = st.selectbox("Выберите стратегию обработки пропущенных значений", 
                                    ["Нет", "Удалить строки", "Заполнить средним", "Заполнить медианой", "Заполнить модой"])
    return missing_strategy
