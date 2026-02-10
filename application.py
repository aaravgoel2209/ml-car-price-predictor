from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load JSON model coefficients and data
with open('LinearRegressionModel.json', 'r') as f:
    MODEL = json.load(f)
car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')

    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    fuel_type = request.form.get('fuel_type')

    # Convert numeric inputs (CRITICAL FIX)
    year = int(request.form.get('year'))
    driven = int(request.form.get('kilo_driven'))

    # Compute linear prediction using JSON coefficients
    intercept = MODEL['intercept']
    coef_year = MODEL['numeric'].get('year', 0.0)
    coef_kms = MODEL['numeric'].get('kms_driven', 0.0)

    y = intercept + coef_year * year + coef_kms * driven

    # Add categorical contributions (OneHot coefficients)
    y += MODEL['categorical']['name'].get(car_model, 0.0)
    y += MODEL['categorical']['company'].get(company, 0.0)
    y += MODEL['categorical']['fuel_type'].get(fuel_type, 0.0)

    return str(np.round(y, 2))


if __name__ == '__main__':
    app.run(debug=False)
