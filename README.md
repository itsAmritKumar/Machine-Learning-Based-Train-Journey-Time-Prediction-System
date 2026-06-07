# 🚆 Train Journey Duration Prediction System

A Machine Learning-based web application that predicts **train journey duration** using railway route and schedule information. The project was developed as part of a Machine Learning Internship at **Sysslan IT Solutions** and demonstrates the complete machine learning workflow including data preprocessing, feature engineering, exploratory data analysis, model training, evaluation, and deployment through Streamlit.

## 📂 Dataset Overview

The dataset contains railway route and schedule information for multiple trains.

### Dataset Features

| Column Name        | Description                            |
| ------------------ | -------------------------------------- |
| `Train_No`         | Unique train number                    |
| `Station_Name`     | Name of the station                    |
| `Arrival_Time`     | Train arrival time at station          |
| `Departure_Time`   | Train departure time from station      |
| `Distance`         | Distance covered from source station   |
| `Route_Number`     | Route identifier                       |
| Other Fare Columns | Fare information for different classes |

### Engineered Features

The following features were created during preprocessing:

| Feature             | Description                                     |
| ------------------- | ----------------------------------------------- |
| `Total_Distance`    | Total distance covered by train                 |
| `Num_Stops`         | Total number of stops in the route              |
| `Departure_Hour`    | Departure hour extracted from source station    |
| `Arrival_Hour`      | Arrival hour extracted from destination station |
| `Distance_Per_Stop` | Average distance covered per stop               |

### Target Variable

| Variable                 | Description                           |
| ------------------------ | ------------------------------------- |
| `Journey_Duration_Hours` | Total train journey duration in hours |

---

## 📊 Project Workflow

### 1. Data Understanding

* Dataset inspection
* Missing value analysis
* Duplicate record detection
* Statistical analysis
* Train-wise source and destination identification

### 2. Data Cleaning & Feature Engineering

* Time format conversion
* Journey duration calculation
* Distance aggregation
* Number of stops calculation
* Creation of machine-learning-ready features

### 3. Exploratory Data Analysis (EDA)

* Distance vs Journey Duration analysis
* Number of Stops vs Journey Duration analysis
* Correlation Heatmap
* Journey Duration Distribution
* Train-wise Stops Pivot Table

### 4. Model Training & Evaluation

* Train-Test Split
* Linear Regression Model
* Performance Evaluation using:

  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * R² Score

### 5. Model Comparison

* Basic Model (Distance only)
* Improved Model (Multiple Features)
* Performance Comparison
* Best Model Selection

### 6. Interactive Web Application

* User-friendly prediction interface
* Real-time duration prediction
* Journey summary visualization
* Model performance display

---

## 🚀 Features & Usage

### Journey Duration Prediction

Enter:

* 🚉 Total Distance (km)
* 🚏 Number of Stops
* 🕒 Departure Time
* 🕒 Arrival Time

The system predicts:

* ⏳ Estimated Journey Duration
* 📋 Journey Summary
* 📊 Duration Visualization

---

## 📈 Model Performance

### Final Selected Model

| Metric   | Score      |
| -------- | ---------- |
| MAE      | 2.38 Hours |
| RMSE     | 3.71 Hours |
| R² Score | 0.52       |

The improved model outperformed the baseline model by incorporating engineered features such as departure hour, arrival hour, and distance per stop.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

## 📁 Project Structure

```text
Train-Journey-Time-Prediction/
│
├── app.py
├── train_journey_model.pkl
├── requirements.txt
├── Train_Journey_Prediction.ipynb
├── README.md
```

---

## 👨‍💻 Developed By

**Amrit Kumar**

📧 Email: [iamamrit79@gmail.com](mailto:iamamrit79@gmail.com)

🔗 LinkedIn: [https://www.linkedin.com/in/amrit-kumar-9a214429b](https://www.linkedin.com/in/amrit-kumar-9a214429b)

---

## 📜 Internship

This project was completed as part of the **Machine Learning Internship Program at Sysslan IT Solutions**.
