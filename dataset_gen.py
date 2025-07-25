import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 10000
age = np.random.randint(18, 80, size=n_samples)
family_history = np.random.choice([0, 1], size=n_samples)  # 0: No, 1: Yes
veg_per_week = np.random.randint(0, 14, size=n_samples)    # servings per week
smoking_status = np.random.choice([0, 1], size=n_samples)  # 0: Non-smoker, 1: Smoker
diabetes = np.random.choice([0, 1], size=n_samples)        # 0: No, 1: Yes
screen_time = np.random.randint(0, 13, size=n_samples)     # hours per day
corrective_lenses = np.random.choice([0, 1], size=n_samples) # 0: No, 1: Yes
uv_exposure = np.random.randint(0, 9, size=n_samples)      # hours per day
gender = np.random.choice([0, 1], size=n_samples)          # 0: Female, 1: Male
physical_activity = np.random.randint(0, 11, size=n_samples) # hours per week
socioeconomic_status = np.random.choice([0, 1, 2], size=n_samples) # 0: Low, 1: Medium, 2: High
access_to_healthcare = np.random.choice([0, 1], size=n_samples) # 0: Poor, 1: Good

# Simulate eye_problem based on expanded logic
eye_problem_score = (
    (age > 50).astype(int) +
    (family_history == 1).astype(int) +
    (veg_per_week < 3).astype(int) +
    (smoking_status == 1).astype(int) +
    (diabetes == 1).astype(int) +
    (screen_time > 6).astype(int) +
    (corrective_lenses == 1).astype(int) +
    (uv_exposure > 4).astype(int) +
    (physical_activity < 2).astype(int) +
    (socioeconomic_status == 0).astype(int) +
    (access_to_healthcare == 0).astype(int)
)
# Convert to binary: 1 if score >= 4, else 0
eye_problem = (eye_problem_score >= 4).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'family_history': family_history,
    'veg_per_week': veg_per_week,
    'smoking_status': smoking_status,
    'diabetes': diabetes,
    'screen_time': screen_time,
    'corrective_lenses': corrective_lenses,
    'uv_exposure': uv_exposure,
    'gender': gender,
    'physical_activity': physical_activity,
    'socioeconomic_status': socioeconomic_status,
    'access_to_healthcare': access_to_healthcare,
    'eye_problem': eye_problem
})

# Save to CSV
df.to_csv('eye_dataset.csv', index=False)

# Prepare X and y
X = df.drop(columns=['eye_problem'])
y = df['eye_problem']