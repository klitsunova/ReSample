import streamlit as st
from modules import upload, preprocess, balance, visualize, recommendations
import assets.markdown as markdown

markdown.set_markdown()
df = upload.upload_dataset()
if 'df' in locals() and df is not None:
    visualize.show_dataset_preview(df)
    df = preprocess.show_preprocessing_options(df)
    target_column = balance.get_target_column(df)
    if target_column is not None:
        visualize.show_distribution(df, target_column)
        recommendations.show_recommendations(df, target_column)
        sampling_strategy = balance.get_sampling_strategy()
        sampling_method = balance.get_sampling_method()
        if sampling_strategy is not None and sampling_method is not None:
            try:
                df_balanced = balance.balance_data(df, target_column, sampling_method, sampling_strategy)
                visualize.show_charts(df, df_balanced, target_column)
                visualize.show_summary(df, df_balanced, target_column)
                visualize.show_download_button(df_balanced)
            except ValueError as e:
                st.write("Something went wrong :( The method may be not suitable for this dataset or ratio.")
                st.write("Try to preprocess missing values if you don't or try another sampling method, please.")
                st.write(f"Error message: {e}")
            