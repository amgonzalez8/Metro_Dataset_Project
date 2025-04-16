# 🚇 Metro Equipment Operating Status Prediction

This is a machine learning group project that predicts the **operating status of metro equipment** based on various sensor readings. The model is deployed via a **Streamlit** web application.

---

## 📌 Project Overview

This is a **classification project** that follows the full machine learning pipeline:

- ✅ Data Cleaning & Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Model Training & Evaluation
- ✅ Deployment via Streamlit web app

The model predicts whether equipment is:
- `Off`
- `No Load`
- `Load`
- `Start`
- `Unknown`

---

## 📁 File Structure

```
📦project-folder/
 ┣ 📜 app.py              # Streamlit web app
 ┣ 📜 model_metro.pkl     # Trained classification model
 ┣ 📓 ProjectNotebook.ipynb # Jupyter notebook with EDA and training
 ┣ 📜 README.md           # This file
```

---

## 🚀 How to Run the Project Locally

### 🔧 Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install streamlit scikit-learn pandas numpy
```

### ▶️ Run the App

Make sure the files `app.py` and `model_metro.pkl` are in the same directory.

```bash
streamlit run app.py
```

The app will open in your default web browser.

---

## 📊 Dataset

- The dataset used contains sensor data from metro equipment systems.
- It includes multiple features such as temperature, pressure, electrical readings, oil levels, and more.
- Size: Over 1,000,000 rows.

---

## 📈 Model

- The model was trained using a classification algorithm (e.g., Random Forest or similar).
- Evaluation metrics include accuracy, precision, recall, and F1-score.
- Saved using `pickle` and loaded in the app.

---

## 💻 Web Application

- Built with **Streamlit**.
- Users input 15 sensor values.
- App returns the predicted operating status of the equipment.

---

## 👥 Group Members

- **C0923004** | Argenis Israel Saldaña Matos  
- **C0923963** | Laura Camila Torres Garzon  
- **C0927303** | Manuela Gonzalez  

---

## 📅 Final Presentation

- The project will be presented live during the last week of the course.
- All group members will demonstrate and explain different parts of the project.

---

## ✅ Evaluation Criteria Checklist

| Criteria               | Included? |
|------------------------|-----------|
| Data Cleaning & EDA    | ✅         |
| Model Performance      | ✅         |
| Web Application        | ✅         |
| Team Presentation      | ✅ (To be done live) |
| README Instructions    | ✅         |

---

## 📬 Contact

For any questions, contact any group member or your instructor.
