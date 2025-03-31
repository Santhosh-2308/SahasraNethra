import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load test data
X_val = np.load("X_val.npy")
y_val = np.load("y_val.npy")

# Load the trained model
model = keras.models.load_model("wildfire_model.h5")

# Evaluate the model
loss, accuracy = model.evaluate(X_val, y_val)

print(f" Model Evaluation Complete:")
print(f"=9 Loss: {loss:.4f}")
print(f"=9 Accuracy: {accuracy:.4f}")
