# Respiratory Sound Diagnosis Using Correlation-Based Features

This repository presents an end-to-end machine learning pipeline for
classifying healthy individuals and asthma patients using correlation
maps derived from multi-channel tracheal respiratory sounds.

The project is based on my undergraduate thesis in Electrical and Electronics Engineering
and focuses on interpretable, signal-driven feature extraction.

---

## 📌 Project Overview

Respiratory sounds captured from multiple tracheal microphones contain
spatial and temporal information that can be leveraged for diagnosis.
This study explores correlation-based representations of these signals
and evaluates their effectiveness using classical machine learning models.

---

## 🧠 Methodology

1. Signal preprocessing (normalization, band-pass filtering)
2. Multi-channel correlation map generation
3. Feature extraction using row-wise correlation patterns
4. Classification using Bayesian and SVM models
5. Evaluation with Leave-One-Out Cross-Validation (LOOCV)

---

## 📂 Repository Structure

respiratory-sound-diagnosis-ml/
├── notebooks/ # Step-by-step analysis notebooks
├── src/ # Modular Python implementations
├── figures/ # Saved correlation maps & confusion matrices
├── docs/ # Thesis summary
├── data/ # Dataset description (no raw data shared)
└── README.md


---

## 📊 Results

Representative results and visualizations can be found in the `figures/` directory:
- Correlation maps highlighting structural differences
- Confusion matrices for Bayesian and SVM classifiers

---

## ⚠️ Data Availability

Due to ethical and privacy considerations, the raw respiratory sound data
cannot be shared publicly. The repository provides complete reproducible
code using representative data structures.

---

## 🚀 Future Work

- Integration of deep learning models
- Larger and more diverse datasets
- Real-time respiratory monitoring applications

---

## 📫 Contact

- **LinkedIn:** https://www.linkedin.com/in/%C3%B6zg%C3%BCr-ar%C4%B1sl%C4%B1el-60478a266/)
- **GitHub:** https://github.com/ozgurangers
