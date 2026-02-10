# ML Car Price Predictor

A simple end-to-end project that cleans a scraped car listings dataset, trains a regression model, and serves a web UI + API to predict used car prices.

## What This Is
- A cleaned dataset and a trained Linear Regression model
- A Flask app with a modern UI for predictions
- A minimal API endpoint for programmatic access
- A notebook showing data cleaning, EDA, and model training

## Quick Start

### 1) Install dependencies (via pyproject)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

### 2) Run the app
```bash
python application.py
```
App starts on http://127.0.0.1:5000

### 3) Use the UI
Open the homepage and fill in company, model, year, fuel type and kilometers driven. Click Predict to see the estimated price.

### 4) Call the API
Predict via POST `/predict`:
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -F "company=Maruti" \
  -F "car_models=Maruti Suzuki Swift" \
  -F "year=2019" \
  -F "fuel_type=Petrol" \
  -F "kilo_driven=100"
```
Response is a numeric price (INR).

## Project Files
- [application.py](application.py) — Flask app (serves UI and `/predict`)
- [templates/index.html](templates/index.html) — Web UI template (Jinja + Bootstrap)
- [static/css/style.css](static/css/style.css) — Styling for the UI
- [quikr-predictor.ipynb](quikr-predictor.ipynb) — Notebook with cleaning, EDA, and model training
- [quikr_car.csv](quikr_car.csv) — Raw dataset
- [Cleaned_Car_data.csv](Cleaned_Car_data.csv) — Cleaned dataset used for app options
- [LinearRegressionModel.pkl](LinearRegressionModel.pkl) — Saved pipeline model
- [pyproject.toml](pyproject.toml) — Python dependencies and metadata

## How It Works
1. The notebook cleans and prepares the data, then trains a Linear Regression pipeline with OneHotEncoder for categorical features.
2. The trained pipeline is saved to [LinearRegressionModel.pkl](LinearRegressionModel.pkl).
3. The Flask app loads the model and the cleaned dataset to populate dropdowns and run predictions (debug disabled by default).

### Evaluation and Metrics
- Test split and cross-validation are used to assess performance.
- Reported metrics: R², MAE, RMSE, and MAPE.
- Both 10-fold K-Fold and RepeatedKFold are included for robust estimates.

## Notes
- Notebook text is concise and professional; sections focus on essentials.
- Dropdown options are powered by the cleaned dataset; if you retrain, regenerate it.
- Predictions expect realistic combinations of features for best results.

## Retraining (Optional)
Open the notebook and run it end-to-end:
- [quikr-predictor.ipynb](quikr-predictor.ipynb)
- The notebook saves `LinearRegressionModel.pkl`; restart the app after retraining.

### Recommended tweaks
- Try regularized models (Ridge/Lasso) and tree-based models (RandomForest, XGBoost).
- Feature engineering (log transforms, interactions) can improve error metrics.

## Tech Stack
- Python, Flask, Jinja2
- pandas, scikit-learn, numpy
- Bootstrap + custom CSS

## Future Ideas
- Model benchmarking dashboard with CV metrics summary
- Batch prediction endpoint
- Containerize with Docker for deployment