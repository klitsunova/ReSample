import streamlit as st
from modules import upload, preprocess, balance, visualize, download
import assets.markdown as markdown

df = upload.upload_dataset()
if 'df' in locals() and df is not None:
    visualize.show_dataset_preview(df)
    df = preprocess.show_preprocessing_options(df)
    target_column = balance.get_target_column(df)
    if target_column is not None:
        visualize.show_distribution(df, target_column)
        sampling_strategy = balance.get_sampling_strategy()
        sampling_method = balance.get_sampling_method()
        if sampling_strategy is not None and sampling_method is not None:
            df_balanced = balance.balance_data(df, target_column, sampling_method, sampling_strategy)
            visualize.show_charts(df, df_balanced, target_column)
            visualize.show_summary(df, df_balanced, target_column)
            visualize.show_download_button(df_balanced)