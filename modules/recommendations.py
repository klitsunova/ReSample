from sklearn.ensemble import VotingRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRegressor
import streamlit as st
import pandas as pd
import numpy as np
import joblib

def get_dataset_info(df, target_column):
    size = len(df)

    class_counts = df[target_column].value_counts()
    imbalance_ratio = class_counts.min() / class_counts.max()

    unique_classes = df[target_column].nunique()
    classification_type = "binary" if unique_classes == 2 else "multiclass"

    return pd.DataFrame({'Size': [size], 'Imbalance Ratio': [imbalance_ratio], 'Type': [classification_type]})


def get_recommendations(df, target_column):
    dataset_info = get_dataset_info(df, target_column)
    method_combinations, encoders, model = joblib.load("assets/optimized_voting_model.pkl")
    dataset_info['Type'] = encoders['Type'].transform(dataset_info['Type'])

    dataset_info = dataset_info.merge(method_combinations, how='cross')
    predictions = model.predict(dataset_info)

    method_combinations['Oversampling'] = encoders['Oversampling'].inverse_transform(method_combinations['Oversampling'])
    method_combinations['Undersampling'] = encoders['Undersampling'].inverse_transform(method_combinations['Undersampling'])

    results_df = pd.DataFrame({
        'Combination': method_combinations.apply(lambda row: tuple(row), axis=1),
        'Predicted BA': predictions
    })

    return results_df.sort_values(by='Predicted BA', ascending=False).head(10)

def show_recommendations(df, target_column):
    st.subheader("📗 Balancing methods Recommendation")
    st.write("Based on the size of your data set and the imbalance ratio, \
             the following balancing methods may be suitable for you:")
    top_10_methods = get_recommendations(df, target_column)
    for i, row in top_10_methods.iterrows():
        if row['Combination'][0] == 'No':
            st.markdown(f"- {row['Combination'][1]}")
        elif row['Combination'][1] == 'No':
            st.markdown(f"- {row['Combination'][0]}")
        else: 
            st.markdown(f"- {row['Combination'][0]} + {row['Combination'][1]}")