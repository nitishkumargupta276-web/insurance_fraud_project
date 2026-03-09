from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values
    age = float(request.form['age'])
    claim_amount = float(request.form['claim_amount'])
    prev_claims = float(request.form['previous_claims'])
    policy_years = float(request.form['policy_years'])

    # Create feature array
    features = np.array([[age, claim_amount, prev_claims, policy_years]])

    # Prediction
    pred = model.predict(features)[0]

    result = "Fraud" if pred == 1 else "Normal"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)