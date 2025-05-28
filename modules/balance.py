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
            "50:50": 1,
            "80:20": 4,
            "70:30": 7/3
        }
        sampling_strategy = ratio_map[balance_ratio]
        return sampling_strategy
    
def get_sampling_method():
    sampling_method = st.radio("⚖ Choose sampling method:", [None] + list(sampling_methods.keys()), horizontal=True, index=0)
    return sampling_method

def balance_data(df, target_column, sampling_method, sampling_strategy):
    with st.spinner(f"⚙ Applying {sampling_method} balancing..."):
        time.sleep(1)
        X = df.drop(columns=[target_column])
        y = df[target_column]        
        sampler = sampling_methods[sampling_method]

        if (sampling_method == 'TomekLinks' or 
            sampling_method == 'CNN' or
            sampling_method == 'ENN' or
            sampling_method == 'OSS' or 
            sampling_method == 'NCR'):
            st.write("This sampling method doesn't allow user to set sampling ratio, but we can process anyway with default one.")
        else:
            class_counts = y.value_counts()
            majority_count = class_counts.max()
            minority_count = class_counts.min()

            new_majority_count =  minority_count * sampling_strategy
            new_minority_count =  majority_count / sampling_strategy

            if (sampling_method == 'RandomOver' or
                 sampling_method == 'SMOTE' or
                 sampling_method == 'B-SMOTE' or
                 sampling_method == 'B-SMOTE SVM' or
                 sampling_method == 'ADASYN'):
                oversample_strategy = {}
                for cls in class_counts.index:
                    oversample_strategy[cls] = int(new_minority_count) if cls != class_counts.idxmax() else int(class_counts[cls])
                sampler.set_params(sampling_strategy=oversample_strategy)
            else:
                undersample_strategy = {}
                for cls in class_counts.index:
                    undersample_strategy[cls] = int(new_majority_count) if cls == class_counts.idxmax() else int(class_counts[cls])
                sampler.set_params(sampling_strategy=undersample_strategy)

        X_resampled, y_resampled = sampler.fit_resample(X, y)
        return pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=[target_column])], axis=1)