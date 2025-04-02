Project Overview.

This project focuses on predicting diseases using machine learning models, including kidney disease, liver disease, and Parkinson's disease. The goal is to analyze patient data, preprocess it, and train models for accurate classification.

Data Preprocessing.

Handling Missing Values: Imputed using mean/median/mode based on model requirements.
Exploratory Data Analysis (EDA): Conducted statistical analysis, visualizations, and feature distributions.
Multicollinearity Check: Used Correlation Coefficient (CRR) to detect and remove highly correlated features. 
Feature Scaling: Applied MinMaxScaler/StandardScaler based on model requirements.
Encoding Categorical Data: Used binary encoding, label encoding, and one-hot encoding.
Handling Imbalanced Data: Used SMOTE (Synthetic Minority Over-sampling Technique) for balancing classes.

Machine Learning Models.

Logistic Regression,
Decision Tree Classifier,
Random Forest Classifier,
Support Vector Machine (SVM).

Model Evaluation.

Performance metrics used:
    Accuracy,
    Precision,
    Recall,
    F1-Score,
    ROC-AUC Score,
Cross-validation applied to ensure model generalization.

Tools Used: Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, SMOTE.
