import streamlit as st
from imblearn.over_sampling import SMOTE

def balance_data(df, target_column, ratio):
    """Балансировка данных с помощью SMOTE"""
    X, y = df.drop(columns=[target_column]), df[target_column]
    smote = SMOTE(sampling_strategy=ratio, random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=[target_column])], axis=1)

def show_balance_options(df):
    st.header("⚖ Балансировка классов")
    target_column = st.selectbox("Выберите целевой столбец", df.columns)
    balance_ratio = st.radio("Выберите балансировку", ["50:50", "70:30", "80:20"], horizontal=True)
    
    if balance_ratio:
        ratio_map = {"50:50": 1.0, "70:30": 0.7, "80:20": 0.8}
        balanced_df = balance_data(df, target_column, ratio_map[balance_ratio])
        st.success("✅ Датасет успешно сбалансирован!")
        return balanced_df
