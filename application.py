from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model and data
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
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

    input_df = pd.DataFrame(
        [[car_model, company, year, driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    prediction = model.predict(input_df)

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)
