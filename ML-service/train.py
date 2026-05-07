from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

DATASET = "dataset"

# Data Augmentation and Preprocessing
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

# Training Dataset
train = datagen.flow_from_directory(
    DATASET,
    target_size=(224,224),
    batch_size=16,
    class_mode='binary',
    subset='training'
)

# Validation Dataset
val = datagen.flow_from_directory(
    DATASET,
    target_size=(224,224),
    batch_size=16,
    class_mode='binary',
    subset='validation',
    shuffle=False
)

# Load MobileNetV2 Model
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224,224,3)
)

# Freeze Layers
for layer in base_model.layers[:-20]:
    layer.trainable = False

# Add Custom Layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)

# Final Model
model = Model(inputs=base_model.input, outputs=output)

# Compile Model
model.compile(
    optimizer=Adam(0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Early Stopping
early_stop = EarlyStopping(
    monitor='val_accuracy',
    patience=2,
    restore_best_weights=True
)

# Train Model
history = model.fit(
    train,
    validation_data=val,
    epochs=5,
    callbacks=[early_stop]
)

# Accuracy Graph
plt.figure(figsize=(8,5))

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.savefig("accuracy_graph.png")
plt.close()

# Loss Graph
plt.figure(figsize=(8,5))

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig("loss_graph.png")
plt.close()

# Predictions
predictions = model.predict(val)

# Convert Predictions to Binary
y_pred = (predictions > 0.5).astype(int)

# True Labels
y_true = val.classes

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))

# Save Model
model.save("model/model.h5")

print("✅ Model trained and saved")

# Class Labels
print(train.class_indices)