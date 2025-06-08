from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')  # Ou 'model.joblib' selon ton fichier

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    input_array = np.array([data])
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        prediction_text = "️L'employé risque de quitter l'entreprise."
    else:
        prediction_text = "L'employé est susceptible de rester dans l'entreprise."

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
