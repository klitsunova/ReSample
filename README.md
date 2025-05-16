# ReSample

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://github.com/user-attachments/assets/e0b5e7f6-f17b-4fdd-bff1-de6f80c67dd6" width="80">
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)


## Overview
**ReSample** is a web application designed to automatically balance datasets for machine learning tasks. It helps address class imbalances in datasets, improving model generalization and performance. It provides a user-friendly interface to handle missing values, balance class distributions, visualize the results and export the processed dataset.

<img src="https://github.com/user-attachments/assets/40b48ad3-ac7d-4cb1-ac44-cd307f62cd13" width="700">


<img src="https://github.com/user-attachments/assets/c9c648f8-4197-4b19-b33a-ff4647139ebd" width="700">

---

## Live Demo
Experience the deployed with Streamlit app here:  

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?logo=streamlit)](https://resample.streamlit.app/)


---

## Features
1. Upload or use a sample dataset.
2. Handle missing values with various strategies (drop, fiil with median/moda/mean).
3. Balance class distribution:
    - Oversampling:
        - Random Oversampling
        - SMOTE
        - Borderline SMOTE
        - B-SMOTE SVM
        - ADASYN
    - Undersampling:
        - Random Undersampling
        - NearMiss (version 1, 2 and 3)
        - TomekLinks
        - CNN
        - ENN
        - OSS
        - NCR
4. Visualize data before and after balancing (Pie & Bar charts).
5. Export the processed dataset.
