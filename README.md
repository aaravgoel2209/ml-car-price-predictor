# ML Car Price Predictor

A simple end-to-end project that cleans a scraped car listings dataset, trains a regression model, and serves a web UI + API to predict used car prices.

## What This Is
- A cleaned dataset and a trained Linear Regression model
- A Flask app with a modern UI for predictions
- A minimal API endpoint for programmatic access
- A notebook showing data cleaning, EDA, and model training

## Quick Start

### 1) Install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
- [requirements.txt](requirements.txt) — Python dependencies

## How It Works
1. Notebook cleans and prepares the data, then trains a Multiple Linear Regression model with OneHotEncoder for categorical features.
2. The trained pipeline is saved to [LinearRegressionModel.pkl](LinearRegressionModel.pkl).
3. The Flask app loads the model and the cleaned dataset to populate dropdowns and run predictions.

## Notes
- The UI is optimized for a dark theme; focus states are customized.
- Dropdown options are powered by the cleaned dataset; if you retrain, regenerate it.
- Predictions expect realistic combinations of features for best results.

## Retraining (Optional)
If you want to tweak or improve the model, open the notebook and run it end-to-end:
- [quikr-predictor.ipynb](quikr-predictor.ipynb)
- Save the new pipeline as `LinearRegressionModel.pkl` and restart the app.

## Tech Stack
- Python, Flask, Jinja2
- pandas, scikit-learn, numpy
- Bootstrap + custom CSS

## Future Ideas
- Try tree-based models (Random Forest, XGBoost)
- Add k-fold cross-validation
- Add endpoints for batch predictions
- Containerize with Docker for easy deployment