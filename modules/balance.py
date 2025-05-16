import streamlit as st
import pandas as pd 
import time

from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import BorderlineSMOTE
from imblearn.over_sampling import SVMSMOTE
from imblearn.over_sampling import ADASYN

from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import TomekLinks
from imblearn.under_sampling import CondensedNearestNeighbour
from imblearn.under_sampling import EditedNearestNeighbours
from imblearn.under_sampling import OneSidedSelection
from imblearn.under_sampling import NeighbourhoodCleaningRule

sampling_methods = {
    'RandomOver': RandomOverSampler(),
    'SMOTE': SMOTE(),
    'B-SMOTE': BorderlineSMOTE(),
    'B-SMOTE SVM': SVMSMOTE(),
    'ADASYN': ADASYN(),

    'RandomUnder': RandomUnderSampler(),
    'NearMiss-1': NearMiss(version=1),
    'NearMiss-2': NearMiss(version=2),
    'NearMiss-3': NearMiss(version=3),
    'TomekLinks': TomekLinks(),
    'CNN': CondensedNearestNeighbour(),
    'ENN': EditedNearestNeighbours(),
    'OSS': OneSidedSelection(),
    'NCR': NeighbourhoodCleaningRule(),
}

def get_target_column(df):
    return st.selectbox("🎯 Select the target variable:", [None] + list(df.columns), index=0, key='target_variable')

def get_sampling_strategy():
    balance_ratio = st.radio("⚖ Choose balance ratio:", [None, "50:50", "70:30", "80:20"], horizontal=True, index=0)
    if balance_ratio:
        ratio_map = {
            "50:50": 1.0,
            "80:20": 0.8,
            "70:30": 0.7
        }
        sampling_strategy = ratio_map[balance_ratio]
        return sampling_strategy
    
def get_sampling_method():
    sampling_method = st.radio("⚖ Choose sampling method:", list(None) + list(sampling_methods.keys()), horizontal=True, index=0)
    return sampling_method

def balance_data(df, target_column, sampling_method, sampling_strategy):
    with st.spinner(f"⚙ Applying {sampling_method} balancing..."):
        time.sleep(1)
        X = df.drop(columns=[target_column])
        y = df[target_column]
        sampler = sampling_methods[sampling_method]
        sampler.set_params(sampling_strategy = sampling_strategy)

        X_resampled, y_resampled = sampler.fit_resample(X, y)
        return pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=[target_column])], axis=1)