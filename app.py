from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Initialize the Flask application
app = Flask(_name_)

# Load the trained model
model = load_model('lungs_disease_model.h5')

# Define the classes with detailed descriptions, symptoms, and precautions
class_info = {
    'Bacterial Pneumonia': {
        'description': 'An infection of the lungs caused by bacteria.',
        'symptoms': 'Cough, Chest pain, Fever, Chills, Shortness of breath',
        'precautions': 'Avoid close contact with infected people, Wash your hands regularly, Get vaccinated if available'
    },
    'Corona Virus': {
        'description': 'A viral infection caused by the SARS-CoV-2 virus.',
        'symptoms': 'Fever, Cough, Shortness of breath, Fatigue, Loss of taste or smell',
        'precautions': 'Wear masks, Maintain social distance, Wash hands frequently, Avoid crowded places'
    },
    'Normal': {
        'description': 'No signs of disease; healthy lung tissue.',
        'symptoms': 'None',
        'precautions': 'Maintain a healthy lifestyle, Avoid smoking, Get regular check-ups'
    },
    'Tuberculosis': {
        'description': 'A serious infectious disease that affects the lungs.',
        'symptoms': 'Persistent cough, Weight loss, Fatigue, Night sweats, Fever',
        'precautions': 'Cover mouth when coughing, Complete TB vaccination, Avoid close contact with infected people'
    },
    'Viral Pneumonia': {
        'description': 'A type of pneumonia caused by viral infections.',
        'symptoms': 'Fever, Dry cough, Headache, Sore throat, Loss of appetite, Muscle pain',
        'precautions': 'Wash your hands regularly, Avoid touching your face, Maintain a healthy immune system'
    }
}

@app.route('/')
def home():
    return render_template('index.html')  # Serve the upload form

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    # Save the uploaded file temporarily
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    # Load and preprocess the image
    img = load_img(file_path, target_size=(224, 224))  # Resize to match model input
    img_array = img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_class = list(class_info.keys())[predicted_index]
    Accuracy = predictions[0][predicted_index] * 100  # Convert to percentage

    # Retrieve details for the predicted class
    description = class_info[predicted_class]['description']
    symptoms = class_info[predicted_class]['symptoms']
    precautions = class_info[predicted_class]['precautions']

    # Clean up the uploaded file
    os.remove(file_path)

    # Generate response with symptoms, precautions, and confidence level
    result = (
        "<div style='font-size: 20px; line-height: 1.6;'>"
        f"<strong>Predicted Class:</strong> {predicted_class}<br>"
        f"<strong>Accuracy:</strong> {Accuracy:.2f}%<br>"
        f"<strong>Description:</strong> {description}<br>"
        f"<strong>Symptoms:</strong> {symptoms}<br>"
        f"<strong>Precautions:</strong> {precautions}"
        "</div>"
    )
    
    return result


if _name_ == '_main_':
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
