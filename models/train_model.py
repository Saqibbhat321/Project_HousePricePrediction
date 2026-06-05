import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("data/Housing.csv")

# Features and target
X = data.drop("price", axis=1)
y = data["price"]

# Categorical columns
categorical_features = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print("R2 Score:", score)

# Save model
with open("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")