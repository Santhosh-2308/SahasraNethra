import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image

# Load the trained model
model = keras.models.load_model("wildfire_model.h5")

def predict_wildfire(img_path="test_fire.jpg"):
    """
    Predicts if a wildfire is detected in the given image.
    
    Parameters:
    img_path (str): Path to the image file.

    Returns:
    str: Prediction result message.
    """
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))  # Resize
        img_array = image.img_to_array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict
        prediction = model.predict(img_array)[0][0]

        # Output result
        if prediction > 0.5:
            return "=% Wildfire Detected!"
        else:
            return " No Wildfire Detected."

    except Exception as e:
        return f"Error: {e}"

# Ensure the script runs properly when executed directly
if __name__ == "__main__":
    result = predict_wildfire()  # Explicitly call the function
    print(result)  # Print the prediction
