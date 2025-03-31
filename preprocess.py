import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

# Define dataset path
dataset_path = "wildfire_dataset"

# Define image size and batch size
IMG_SIZE = (224, 224)  
BATCH_SIZE = 32

# Check if dataset path exists
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"L Dataset folder '{dataset_path}' not found!")

# ImageDataGenerator for preprocessing
datagen = ImageDataGenerator(
    rescale=1.0/255.0,  # Normalize pixel values (0-1)
    validation_split=0.2  # 80% train, 20% validation split
)

# Load training data
train_data = datagen.flow_from_directory(
    dataset_path,  
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

# Load validation data
val_data = datagen.flow_from_directory(
    dataset_path,  
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# Convert the generator output into NumPy arrays
X_train, y_train = [], []
X_val, y_val = [], []

# Loop through the training dataset
for _ in range(len(train_data)):  
    images, labels = next(train_data)  #  Fixed `.next()`
    X_train.extend(images)
    y_train.extend(labels)

# Loop through the validation dataset
for _ in range(len(val_data)):  
    images, labels = next(val_data)  #  Fixed `.next()`
    X_val.extend(images)
    y_val.extend(labels)

# Convert lists to NumPy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)
X_val = np.array(X_val)
y_val = np.array(y_val)

# Save preprocessed data
np.save("X_train.npy", X_train)
np.save("y_train.npy", y_train)
np.save("X_val.npy", X_val)
np.save("y_val.npy", y_val)

print(" Data Preprocessing Done! Saved as .npy files.")
