from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('final_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    
    print("Predict route triggered")

    heart_rate = float(request.form['heartRate'])
    resting_heart_rate = float(request.form['restingHeartRate'])
    bmi = float(request.form['bmi'])
    calories = float(request.form['calories'])
    age = float(request.form['age'])
    gender = int(request.form['gender'])

    # Print the input values for debugging
    print("Input values:")
    print("Heart Rate:", heart_rate)
    print("Resting Heart Rate:", resting_heart_rate)
    print("BMI:", bmi)
    print("Calories:", calories)
    print("Age:", age)
    print("Gender:", gender)

    # Perform prediction using the loaded model
    input_features = [[heart_rate, resting_heart_rate, bmi, calories, age, gender]]
    fas_score = model.predict(input_features)[0]

    # Print the prediction result for debugging
    print("FAS Score:", fas_score)

    # Return the prediction result as a response
    return jsonify({'fasScore': fas_score})


# # Define the route for prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     heart_rate = float(request.form['heartRate'])
#     resting_heart_rate = float(request.form['restingHeartRate'])
#     bmi = float(request.form['bmi'])
#     calories = float(request.form['calories'])
#     age = float(request.form['age'])
#     gender = int(request.form['gender'])

#     # Perform prediction using the loaded model
#     input_features = [[heart_rate, resting_heart_rate, bmi, calories, age, gender]]
#     fas_score = model.predict(input_features)[0]

#     # Define the corresponding fatigue level based on the predicted FAS score
#     fatigue_levels = {
#         0: "No Fatigue",
#         1: "Low Fatigue",
#         2: "Low Fatigue",
#         3: "Moderate Fatigue",
#         4: "Moderate Fatigue",
#     }
#     fatigue_level = fatigue_levels[int(fas_score)]

#     # Prepare the prediction result
#     prediction_result = {
#         'fasScore': fas_score,
#         'fatigueLevel': fatigue_level
#     }

#     return jsonify(prediction_result)

# # Define the route for the landing page
@app.route('/')
def home():
    return render_template('file.html')

if __name__ == '__main__':
    app.run(debug=True)
