# Graduate Admission Predictor

A machine learning project that estimates graduate admission chances using students' academic profiles and application-related factors.

**[Live Demo](https://admission-predictor-22.streamlit.app/) · [GitHub Repository](https://github.com/thamil-sivagnanam/admission-predictor)**

## About the Project

This project explores how regression models can be used to estimate a student's chance of admission based on academic and profile-related information. I worked through the machine learning workflow, from exploring the dataset and comparing models to saving the selected model and building an interactive Streamlit application.

## Dataset

- **Source:** Graduate Admission Dataset (Kaggle)
- **Records:** Approximately 400 student profiles
- **Target:** Chance of Admit (0 to 1)
- **Input features:** GRE Score, TOEFL Score, University Rating, SOP, LOR, GPA, and Research Experience

## Workflow

1. Data exploration and preprocessing
2. Exploratory data analysis
3. Feature analysis
4. Training and comparing regression models
5. Model evaluation
6. Saving the selected model
7. Building the Streamlit prediction interface

## Model Comparison

I trained and compared three regression models using an 80/20 train-test split:

| Model | R² Score | MAE |
|---|---:|---:|
| Linear Regression | 0.9028 | 0.02342 |
| Random Forest Regressor | 0.8520 | 0.02893 |
| XGBoost Regressor | 0.8373 | 0.02966 |

Linear Regression achieved the highest R² score and the lowest MAE among the three models in this experiment. These are test-set results from this dataset split; they should not be interpreted as a guarantee of real-world admission accuracy.

### Feature Analysis

I also compared Random Forest performance with and without the Research feature. In that experiment, the R² score decreased from approximately 0.8520 to 0.2100 when the feature was removed, indicating that it was influential in that model's predictions.

## Application

The Streamlit application accepts seven inputs:

- GRE Score
- TOEFL Score
- University Rating
- SOP
- LOR
- GPA
- Research Experience

It loads the saved Linear Regression model and displays an estimated admission chance with a simple high, moderate, or low category.

![Application screenshot](assets/app.png)

**[Try the Live Application](https://admission-predictor-22.streamlit.app/)**

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Jupyter Notebook

## Run Locally

Clone the repository:

```bash
git clone https://github.com/thamil-sivagnanam/admission-predictor.git
cd admission-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application from the repository root:

```bash
streamlit run app/app.py
```

The application expects the trained model at `model/model.pkl`. The repository also includes the notebook at `notebook/eda_model.ipynb` and the dataset at `data/admission.csv`.

## Author

**Thamil Sivagnanam**  
MSc Artificial Intelligence student at Brandenburg University of Technology (BTU Cottbus).

[GitHub Profile](https://github.com/thamil-sivagnanam)

---

This project was developed for learning and educational purposes. The prediction is an estimate based on the dataset and model, not an actual university admission decision.
