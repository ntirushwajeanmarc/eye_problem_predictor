import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('eye_dataset.csv')

# Features and target
X = df.drop(columns=['eye_problem'])
y = df['eye_problem']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Example: Predict on a new record
# Replace these values with the actual new record's feature values
new_record = pd.DataFrame([{
    'age': 25,
    'family_history': 0,
    'veg_per_week': 0,
    'smoking_status': 0,
    'diabetes': 0,
    'screen_time': 10,
    'corrective_lenses': 0,
    'uv_exposure': 3,
    'gender': 1,
    'physical_activity': 1,
    'socioeconomic_status': 1,
    'access_to_healthcare': 0
}])

prediction = model.predict(new_record)
print("Prediction for new record (1=eye problem, 0=no eye problem):", prediction[0])