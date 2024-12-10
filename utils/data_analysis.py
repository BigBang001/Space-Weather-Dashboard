"""
Data Analysis
Module for predictive modeling of solar events using TensorFlow.
"""

import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "models/solar_event_model.h5"

def predict_solar_events(data):
    """
    Predicts solar events using a pre-trained TensorFlow model.

    Args:
        data (DataFrame): Solar activity data.

    Returns:
        np.array: Predictions for solar events.
    """
    try:
        model = load_model(MODEL_PATH)

        # Prepare input data (normalize or preprocess as per the model)
        input_features = data[["xray_flux", "proton_flux", "electron_flux"]].fillna(0).values
        predictions = model.predict(input_features)
        return predictions
    except Exception as e:
        print(f"Error in prediction: {e}")
        return np.array([])
