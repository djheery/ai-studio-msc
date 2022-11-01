# Creating the model object
model = keras.sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
mdoel.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compiling the model

model.compile(loss='binary_crossentropy', optimzer='adam', metrics=['accuracy'])

# Model Fitting 

model.fit(x_train, y_train, batch_size=32, epochs=15, verbose=1, validation_data=(x_test, y_test))

# Model Evaluation: 

score = model.evaluate(x_test, y_test, batch_size=32)

# Model Prediction: 

model.predict(x_test, batch_size=32)