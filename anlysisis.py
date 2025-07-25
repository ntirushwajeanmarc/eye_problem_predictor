import pandas as pd
from scipy.stats import pointbiserialr

df = pd.read_csv('eye_dataset.csv')

features = [
    'age', 'family_history', 'veg_per_week', 'smoking_status', 'diabetes',
    'screen_time', 'corrective_lenses', 'uv_exposure', 'gender',
    'physical_activity_in_hours', 'socioeconomic_status', 'access_to_healthcare'
]

print("Point-Biserial Correlation with eye_problem:")
for feature in features:
    corr, p = pointbiserialr(df['eye_problem'], df[feature])
    print(f"{feature}: r={corr:.3f}, p-value={p:.3g}")