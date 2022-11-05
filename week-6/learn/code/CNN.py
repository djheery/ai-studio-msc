import tensorflow as tf 
from tensorflow.keras import layers, models

# Creating Model Object 

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu')))
model.add(layers.MaxPooling2D((2, 2))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='sigmoid'))
model.add(layers.Dense(10))

# Compiling the Model 

model.compile(
  optimizer='adam', 
  loss='tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True', 
  metrics=['accuracy']
)

# Model Fitting

tran_images = []
train_labels = []

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Model Prediction 

x_test = []

model.predict(x_test, batch_size=32)

