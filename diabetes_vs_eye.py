import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr

df = pd.read_csv('eye_dataset.csv')

# Bar plot: proportion of eye problems by diabetes status
# Assuming 0: No diabetes, 1: Has diabetes
diabetes_map = {0: 'No Diabetes', 1: 'Diabetes'}
df['diabetes_label'] = df['diabetes'].map(diabetes_map)
diabetes_risk = df.groupby('diabetes_label')['eye_problem'].mean().reset_index()

plt.figure(figsize=(6, 4))
sns.barplot(x='diabetes_label', y='eye_problem', data=diabetes_risk)
plt.title('Proportion of Eye Problems by Diabetes Status')
plt.xlabel('Diabetes Status')
plt.ylabel('Proportion with Eye Problem')
plt.ylim(0, 1)
plt.savefig('eye_problem_by_diabetes.png')
plt.close()

# Correlation coefficient (point-biserial)
corr, p = pointbiserialr(df['eye_problem'], df['diabetes'])
print(f'diabetes: Point-Biserial r={corr:.3f}, p-value={p:.3g}')
