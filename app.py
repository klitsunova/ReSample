import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
import time
from modules import upload, preprocess, balance, visualize, download

def load_styles():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Data Balancer", layout="wide", page_icon="🔄")
st.title("🔄 Synthetic Data Generator")

# Подключение стилей
load_styles()

upload.show_upload()
preprocess.show_preprocessing_options()
balance.show_balance_options()
visualize.show_charts()
download.show_download()