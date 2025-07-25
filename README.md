# Eye Problem Prediction with Synthetic Health Dataset

This project demonstrates how to generate a synthetic health dataset and use machine learning to predict the risk of eye problems based on various lifestyle and health factors. The workflow includes data generation, exploratory analysis, model training, and feature importance evaluation.

## Features

- **Synthetic dataset generation** with realistic health and lifestyle variables
- **Exploratory data analysis** with visualizations and correlation analysis
- **Logistic regression model** for binary classification (eye problem: yes/no)
- **Prediction on new records**
- **Feature importance analysis**

## Dataset

The dataset includes the following features:

- `age`: Age of the individual
- `family_history`: Family history of eye problems (0: No, 1: Yes)
- `veg_per_week`: Vegetable servings per week
- `smoking_status`: Smoking status (0: Non-smoker, 1: Smoker)
- `diabetes`: Diabetes status (0: No, 1: Yes)
- `screen_time`: Daily screen time (hours)
- `corrective_lenses`: Use of corrective lenses (0: No, 1: Yes)
- `uv_exposure`: Daily UV exposure (hours)
- `gender`: Gender (0: Female, 1: Male)
- `physical_activity`: Physical activity per week (hours)
- `socioeconomic_status`: Socioeconomic status (0: Low, 1: Medium, 2: High)
- `access_to_healthcare`: Access to healthcare (0: Poor, 1: Good)
- `eye_problem`: Target variable (0: No eye problem, 1: Eye problem)

## Usage

1. **Generate the dataset:**
   ```bash
   python3 dataset_gen.py
   ```
2. **Train and evaluate the model:**
   ```bash
   python3 trainer.py
   ```
3. **Explore feature relationships:**
   - Run the provided analysis scripts (e.g., `age_vs_eye.py`, `veg_vs_eye.py`, etc.) to visualize and analyze feature influence.

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- scipy

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Project Structure

- `dataset_gen.py`: Synthetic dataset generator
- `trainer.py`: Model training and prediction
- `*_vs_eye.py`: Feature analysis scripts
- `eye_dataset.csv`: Generated dataset

## License

MIT License

---

### GitHub Description

Synthetic health dataset generator and machine learning pipeline for predicting eye problems based on lifestyle and health factors. Includes data generation, exploratory analysis, and logistic regression modeling.
