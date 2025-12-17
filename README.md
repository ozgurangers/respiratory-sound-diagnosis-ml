# Respiratory Sound Diagnosis using Machine Learning

This project presents a machine learning-based diagnostic pipeline for distinguishing healthy individuals from asthma patients using tracheal respiratory sound recordings.

## Problem Statement
Respiratory diseases such as asthma can be identified through acoustic patterns in respiratory sounds. The goal of this project is to design an interpretable and effective ML pipeline based on correlation maps extracted from multi-channel tracheal sound signals.

## Dataset
- Multi-channel tracheal sound recordings
- Subjects labeled as Healthy or Asthma
- Dataset is anonymized and used for academic purposes

> Note: Raw data is not publicly shared due to privacy restrictions.

## Methodology
1. Signal preprocessing
2. Cross-correlation based feature extraction
3. Construction of correlation maps
4. Feature selection
5. Classification using:
   - Bayesian Classifier
   - Support Vector Machine (SVM)

## Evaluation Metrics
- Accuracy
- F1-score
- Confusion Matrix

## Results
The proposed approach demonstrates that correlation-based features are effective in distinguishing respiratory conditions, achieving promising classification performance.

## Technologies Used
- Python
- NumPy, SciPy, Pandas
- scikit-learn
- MATLAB (for validation)

## Author
Özgür Arıslıel  
Machine Learning / AI Engineer (New Graduate)
