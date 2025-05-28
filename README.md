# ReSample

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://github.com/user-attachments/assets/8b1b7f0b-f7c8-457d-b7a9-2c14e19d1b35" width="75">
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)


## Overview
**ReSample** is a web application designed to automatically balance datasets for machine learning tasks. It helps address class imbalances in datasets, improving model generalization and performance. It provides a user-friendly interface to handle missing values, balance class distributions, visualize the results and export the processed dataset.

Additionally, **ReSample** features a **recommendation model** that suggests ten of the most optimal combinations of balancing methods based on the size and imbalance ratio of the uploaded dataset.

<img src="https://github.com/user-attachments/assets/3c4b555a-1fb1-4644-be6f-97eb00515435" width="700">

<img src="https://github.com/user-attachments/assets/dbf114b1-7438-4ced-b41b-5afa5da97478" width="700">

<img src="https://github.com/user-attachments/assets/fb01d179-ea21-4b70-93e8-f2ce2826ace0" width="700">

---

## Live Demo
Experience the deployed with Streamlit app here:  

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?logo=streamlit)](https://resample.streamlit.app/)


---

## Features
1. Upload or use a sample dataset.
2. Handle missing values with various strategies (drop, fiil with median/moda/mean).
3. Get recommendations about balancing methods based on dataset size and imbalance ratio. 
4. Balance class distribution:
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
5. Visualize data before and after balancing (Pie & Bar charts).
6. Export the processed dataset.
