from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained Stacking Classifier model
model = joblib.load('liver_cirrhosis_stacking_model.pkl')

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form input values (11 features)
        age = float(request.form['age'])
        n_days = float(request.form['n_days'])
        sex = 1 if request.form['sex'] == 'M' else 0
        ascites = 1 if request.form['ascites'] == 'Y' else 0
        hepatomegaly = 1 if request.form['hepatomegaly'] == 'Y' else 0
        spiders = 1 if request.form['spiders'] == 'Y' else 0
        edema = 1 if request.form['edema'] == 'Y' else 0
        bilirubin = float(request.form['bilirubin'])
        cholesterol = float(request.form['cholesterol'])
        albumin = float(request.form['albumin'])
        copper = float(request.form['copper'])

        # Prepare the feature array for prediction (11 features)
        features = np.array([[age, n_days, sex, ascites, hepatomegaly, spiders, edema, 
                              bilirubin, cholesterol, albumin, copper]])

        # Make prediction
        prediction = model.predict(features)

        # Return the result
        return render_template('index.html', prediction_text=f'The predicted stage is: {prediction[0]}')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
