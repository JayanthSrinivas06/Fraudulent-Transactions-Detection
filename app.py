# app.py
from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model and scaler
try:
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
except FileNotFoundError:
    print("Error: 'model.pkl' or 'scaler.pkl' not found. Make sure these files are in the same directory.")
    loaded_model = None
    scaler = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST' and loaded_model and scaler:
        amt = float(request.form['amt'])
        zip_code = float(request.form['zip'])
        lat = float(request.form['lat'])
        long_val = float(request.form['long'])
        city_pop = float(request.form['city_pop'])
        merch_lat = float(request.form['merch_lat'])
        merch_long = float(request.form['merch_long'])
        age = float(request.form['age'])
        transaction_hour = int(request.form['transaction_hour'])
        transaction_day_of_week = int(request.form['transaction_day_of_week'])
        transaction_month = int(request.form['transaction_month'])

        # Create a DataFrame with the input features
        input_data = pd.DataFrame({
            'amt': [amt],
            'zip': [zip_code],
            'lat': [lat],
            'long': [long_val],
            'city_pop': [city_pop],
            'merch_lat': [merch_lat],
            'merch_long': [merch_long],
            'age': [age],
            'transaction_hour': [transaction_hour],
            'transaction_day_of_week': [transaction_day_of_week],
            'transaction_month': [transaction_month]
        })

        # Scale numerical features
        numerical_features = ['amt', 'zip', 'lat', 'long', 'city_pop', 'merch_lat', 'merch_long', 'age',
                              'transaction_hour', 'transaction_day_of_week', 'transaction_month']
        numerical_features_present = [col for col in numerical_features if col in input_data.columns]
        if numerical_features_present:
            input_data[numerical_features_present] = scaler.transform(input_data[numerical_features_present])

        # Make prediction
        prediction_probability = loaded_model.predict_proba(input_data)[:, 1][0]
        if prediction_probability > 0.5:
            prediction_result = "Fraud"
        else:
            prediction_result = "Not Fraud"

        return render_template('output.html', prediction=prediction_result)
    else:
        return "Error: Model or scaler not loaded."

if __name__ == '__main__':
    app.run(debug=True)