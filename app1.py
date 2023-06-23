# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor

# app = Flask(__name__)



# def load_model():
#     global best_model 
#     best_model = pickle.load(open('final_model.pkl', 'rb'))

# # Load the model before running the app
# load_model()

# @app.route('/')
# def home():
#     return render_template('file.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     int_features = [float(x) for x in request.form.values()]
#     features = [np.array(int_features)]
#     prediction = best_model.predict(features)

#     output = round(prediction[0], 2)
#     return render_template('final.html', prediction_text='Predicted FAS score is {}'.format(output))

# if __name__ == '__main__':
#     app.run()
# from flask import Flask, render_template, request
# import joblib
# import numpy as np

# app = Flask(__name__)

# model = joblib.load("final_model.pkl")

# @app.route('/')
# def home():
#     return render_template('file.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     hear_rate = float(request.form.get('hear_rate'))
#     calories = float(request.form.get('calories'))
#     BMI = float(request.form.get('BMI'))
#     resting_heart = float(request.form.get('resting_heart'))
#     age = float(request.form.get('age'))
#     gender_str = request.form.get('gender')

#     gender = 0 if gender_str == '0' else 1


#     features = np.array([[hear_rate, calories, BMI, resting_heart, age, gender]])
#     prediction = model.predict(features)
    

#     output = round(prediction[0], 2)

#     return render_template('./file.html', prediction_text='Predicted FAS score is {}'.format(output) )

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("C:/Users/DELL/Desktop/Fatigue-Detection-Model/final_model.pkl")

fatigue_levels = {
    0: "No Fatigue",
    1: "Low Fatigue",
    2: "Low Fatigue",
    3: "Moderate Fatigue",
    4: "High Fatigue"
}

@app.route('/')
def home():
    return render_template('file.html')

@app.route('/predict', methods=['POST'])
def predict():
    hear_rate = float(request.form.get('hear_rate'))
    calories = float(request.form.get('calories'))
    BMI = float(request.form.get('BMI'))
    resting_heart = float(request.form.get('resting_heart'))
    age = float(request.form.get('age'))
    gender_str = request.form.get('gender')

    gender = 0 if gender_str == '0' else 1

    features = np.array([[hear_rate, calories, BMI, resting_heart, age, gender]])
    prediction = model.predict(features)

    output = round(prediction[0], 2)

    fatigue_level = fatigue_levels.get(int(output), "Invalid FAS score")
    if output > 10:
        fatigue_level = "Average Fatigue"

    return render_template('./file.html', prediction_text='Predicted FAS score is {}. Fatigue Level: {}'.format(output, fatigue_level), 
                           hear_rate_value=hear_rate,
                           calories_value=calories,
                           BMI_value=BMI,
                           resting_heart_value=resting_heart,
                           age_value=age,
                           gender_value=gender_str)


if __name__ == '__main__':
    app.run()




