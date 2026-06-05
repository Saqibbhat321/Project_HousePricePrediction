# 🏠 House Price Prediction System

A Machine Learning web application that predicts house prices based on various property features such as area, bedrooms, bathrooms, parking availability, furnishing status, and other housing attributes.

---

# 📌 Project Overview

This project uses a real-world housing dataset containing 545 records and multiple numerical and categorical features.

The application performs:

* Data Loading
* Data Preprocessing
* Feature Engineering
* Categorical Encoding
* Model Training
* Model Evaluation
* House Price Prediction
* Web Application Deployment

The final model is deployed using Streamlit, allowing users to enter house details and receive an estimated property price.

---

# 🚀 Features

✅ Real-world Housing Dataset

✅ Data Preprocessing using ColumnTransformer

✅ One-Hot Encoding for Categorical Features

✅ Random Forest Regression Model

✅ Model Evaluation using R² Score

✅ Interactive Streamlit Web Interface

✅ Model Serialization using Pickle

✅ End-to-End Machine Learning Workflow

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Pickle

---

# 📂 Project Structure

```text
HousePricePrediction/
│
├── data/
│   └── Housing.csv
│
├── models/
│   └── train_model.py
│
├── app.py
│
├── house_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset Information

Dataset Features:

| Feature          | Description                   |
| ---------------- | ----------------------------- |
| area             | Area of house in square feet  |
| bedrooms         | Number of bedrooms            |
| bathrooms        | Number of bathrooms           |
| stories          | Number of floors              |
| mainroad         | Access to main road           |
| guestroom        | Availability of guest room    |
| basement         | Basement availability         |
| hotwaterheating  | Hot water heating facility    |
| airconditioning  | Air conditioning availability |
| parking          | Number of parking spaces      |
| prefarea         | Located in preferred area     |
| furnishingstatus | Furnishing status             |
| price            | Target variable (House Price) |

Dataset Size:

* Rows: 545
* Columns: 13

---

# 🧠 Machine Learning Concepts Used

## Data Preprocessing

Applied preprocessing techniques to convert categorical variables into machine-readable format.

### OneHotEncoder

Used to convert categorical values such as:

```text
yes/no
furnished
semi-furnished
unfurnished
```

into numerical representations.

---

## ColumnTransformer

Used to apply transformations only to categorical columns while keeping numerical columns unchanged.

---

## Pipeline

Used to combine preprocessing and machine learning model training into a single workflow.

Benefits:

* Cleaner code
* Consistent preprocessing
* Reduced data leakage
* Easier deployment

---

# 🤖 Machine Learning Model

Algorithm Used:

## Random Forest Regressor

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Advantages:

* High accuracy
* Handles mixed data types
* Robust against overfitting
* Works well on real-world datasets

Model Parameters:

```python
RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
```

---

# 📈 Model Evaluation

Metric Used:

## R² Score

R² Score measures how well the model explains variations in house prices.

Interpretation:

| R² Score  | Performance        |
| --------- | ------------------ |
| 1.0       | Perfect Prediction |
| 0.8+      | Excellent Model    |
| 0.6 - 0.8 | Good Model         |
| < 0.5     | Needs Improvement  |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/HousePricePrediction.git
cd HousePricePrediction
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

Run:

```bash
python models/train_model.py
```

Output:

```text
R2 Score: 0.85
Model Saved Successfully!
```

A file named:

```text
house_model.pkl
```

will be generated.

---

# ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 💻 Example Prediction

### Input

```text
Area = 6000
Bedrooms = 4
Bathrooms = 3
Stories = 2
Main Road = Yes
Guest Room = Yes
Basement = No
Parking = 2
Furnishing Status = Furnished
```

### Output

```text
Estimated House Price:
₹ 8,500,000
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Data Loading and Analysis
* Feature Selection
* Data Preprocessing
* One-Hot Encoding
* ColumnTransformer
* Pipeline Creation
* Random Forest Regression
* Model Evaluation
* Model Serialization
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

# 📚 Future Improvements 


* Hyperparameter Tuning
* Feature Importance Analysis
* Cross Validation
* Model Comparison
* XGBoost Implementation
* Deployment on Cloud Platforms
* Advanced Data Visualization Dashboard

---

# 📸 Application Screenshots


<img width="721" height="1189" alt="housepridic" src="https://github.com/user-attachments/assets/340d9302-7a2c-4a0b-b841-2104de72cf31" />


---

# 👨‍💻 Author

Saqib Bhat

---

# ⭐ Project Summary

Developed an end-to-end House Price Prediction System using Python, Pandas, Scikit-Learn, and Streamlit. Implemented data preprocessing using OneHotEncoder and ColumnTransformer, built a Pipeline-based Random Forest Regression model, evaluated performance using R² Score, and deployed the solution through an interactive web application for real-time house price prediction.
