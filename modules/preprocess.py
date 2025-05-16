import streamlit as st
import pandas as pd

def show_preprocessing_options(df):
    if df.isnull().sum().sum() > 0:
        st.warning("⚠️ Missing values detected in the dataset.")
        st.write("### Missing Values Summary")
        st.write(df.isnull().sum().rename('Missing Value Counts'))
        missing_option = st.selectbox("🧹 Choose a missing value handling strategy:", ["None", "Drop Rows", "Fill with Mean", "Fill with Median","Fill with Mode"], key='missing_strategy')
        if missing_option == "Drop Rows":
            df.dropna(inplace=True)
            st.success("✅ Missing values have been removed.")
        elif missing_option == "Fill with Mean":
            df.fillna(df.mean(), inplace=True)
            st.success("✅ Missing values have been filled with column means.")
        elif missing_option == "Fill with Median":
            df.fillna(df.median(), inplace=True)
            st.success("✅ Missing values have been filled with column medians.")
        elif missing_option == "Fill with Mode":
            df.fillna(df.mode().iloc[0], inplace=True)
            st.success("✅ Missing values have been filled with column modes.")
    return df
