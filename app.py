from flask import Flask, render_template, request
import numpy as np
import traceback

app = Flask(__name__)

# Load your machine learning model (assuming you have the model file loaded here)
# model = load_your_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieving and validating form data
        input_data = [
            int(request.form.get('day_of_week', 0)),
            int(request.form.get('educational_level', 0)),
            int(request.form.get('driving_experience', 0)),
            int(request.form.get('type_of_vehicle', 0)),
            int(request.form.get('owner_of_vehicle', 0)),
            int(request.form.get('area_accident_occured', 0)),
            int(request.form.get('road_alignment', 0)),
            int(request.form.get('types_of_junction', 0)),
            int(request.form.get('road_surface_type', 0)),
            int(request.form.get('road_surface_conditions', 0)),
            int(request.form.get('light_conditions', 0)),
            int(request.form.get('weather_conditions', 0)),
            int(request.form.get('cause_of_accident', 0)),  # Cause of Accident field
            int(request.form.get('type_of_collision', 0)),
            int(request.form.get('number_of_vehicles_involved', 1)) if request.form.get('number_of_vehicles_involved') else 1,  # Default to 1
            int(request.form.get('vehicle_movement', 0))
        ]

        # Placeholder prediction logic (replace with your ML model prediction)
        input_array = np.array(input_data).reshape(1, -1)
        prediction = np.random.choice([0, 1, 2])  # Random prediction for demonstration

        severity_mapping = {0: 'Slight Injury', 1: 'Serious Injury', 2: 'Fatal Injury'}
        result = severity_mapping.get(prediction, 'Unknown Severity')

        return render_template('index.html', prediction_text=f'Predicted Accident Severity: {result}')

    except Exception as e:
        error_message = traceback.format_exc()
        return render_template('index.html', prediction_text=f'Error occurred: {str(e)}\nDetails: {error_message}')

if __name__ == '__main__':
    app.run(debug=True)