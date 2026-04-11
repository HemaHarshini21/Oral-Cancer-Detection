from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

DATASET = "dataset"

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train = datagen.flow_from_directory(
    DATASET,
    target_size=(224,224),
    batch_size=16,
    class_mode='binary',
    subset='training'
)

val = datagen.flow_from_directory(
    DATASET,
    target_size=(224,224),
    batch_size=16,
    class_mode='binary',
    subset='validation'
)

base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))

for layer in base_model.layers[:-20]:
    layer.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer=Adam(0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(train, validation_data=val, epochs=10)

model.save("model/model.h5")

print("✅ Model trained and saved")

print(train.class_indices)