from flask import Flask, render_template, request, jsonify
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('C:\\HeartDiseasePrediction\\app\\model\\heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', title = "Home")

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()

    # Extract features from the JSON data
    features = [
        data['age'], data['sex'], data['cp'],
        data['trestbps'], data['chol'],
        data['fbs'], data['restecg'],
        data['thalach'], data['exang'],
        data['oldpeak'], data['slope'], data['ca'],
        data['thal']
    ]

    # Make a prediction
    predictions = model.predict([features])[0]

    # Return the result as JSON
    result = {
        'prediction': int(predictions),
        'message': "The person has heart disease" if predictions == 1 else "The person does not have heart disease"
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
