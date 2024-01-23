#==================================================#
# Module: PE7047 (AI Studio)                   	#
# Deadline: 18th December 2022                 	#
# Student ID: W21045778                        	#
# Student Name: Daniel Heery                   	#
#==================================================#

import keras
import tensorflow
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.optimizers import SGD
from keras.datasets import cifar10
from sklearn.model_selection import KFold
from keras.callbacks import ReduceLROnPlateau
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
%matplotlib inline

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Printing the Shape of the Training data
print('x_train shape: ', x_train.shape)
print('y_train shape: ', y_train.shape)

# Printing the Shape of the Test Data
print('x_test shape', x_test.shape)
print('y_test shape', y_test.shape)

## One Hot Encoding

y_train_one_hot = keras.utils.to_categorical(y_train, 10)
y_test_one_hot = keras.utils.to_categorical(y_test, 10)

## Image Processing

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train / 255
x_test = x_test / 255


# Plot the dataset to review class balance/imbalance
"""
  Plot the bar graph for Classification balance metric analysis
  @data - A sorted dataset formatted for the purposes for displaying a bar graph
  @title - The title of the graph to be produced

  For reference:
  The x labels are as follows:
  0: airplane
  1: automobile
  2: bird
  3: cat
  4: deer
  5: dog
  6: from
  7: horse
  8: ship
  9: truck
"""

def plot_bar_for_balance_metrics(data, title):
  plt.bar(range(len(data)), [d[1] for d in data], align='center')
  plt.xticks(range(len(data)), [d[0] for d in data])
  plt.title(title)
  plt.xlabel('classes')
  plt.ylabel('Class Count')
  plt.show()

"""
  A method for formatting/ y_train and y_test datasets to be displayed on a bar graph
  @train - the train data
  @test - the test data
"""
def prepare_for_balance_metrics(train, test) :
  train = sorted(Counter(train.flatten()).items())
  test = sorted(Counter(test.flatten()).items())
  plot_bar_for_balance_metrics(train, "Train Dataset Class Balance")
  plot_bar_for_balance_metrics(test, "Test Dataset Class Balance")

prepare_for_balance_metrics(y_train, y_test)

# Define all models

# Baseline Model (BM)
def original_model() :
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)))
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.25))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Flatten())
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='softmax'))
  return model

# Final Model Architecture
def final_model() :
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)))
  model.add(BatchNormalization())
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.3))
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.4))
  model.add(Flatten())
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='softmax'))
  return model

  # Final Model with Deeper Architecture (Removed from comparisons due to a lack of space)
 
def final_model_deep() :
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)))
  model.add(BatchNormalization())
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.3))
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.4))
  model.add(Flatten())
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='softmax'))
  return model

# Final Model Architecture without Batch Normalization

def final_model_no_batch() :
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)))
  model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.3))
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.4))
  model.add(Flatten())
  model.add(Dense(512, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='softmax'))
  return model

# Print Final Model Summary
final_model().summary()

# Define Hyperparameters and Callbacks

# Hyper Parameters
epoch_num_og = 20
epoch_num = 40
batch_size_og = 32
batch_size_final = 16
validation_split_percentage = 0.2
metrics_arr = ['accuracy']
sgd_final=SGD(learning_rate=0.002, momentum=0.9)
sgd_no_momentum=SGD(learning_rate=0.002)
split_num = 5
isShuffled = True

# Callbacks (Unused in submitted work, just used in initial experiments)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                          	patience=5, min_lr=1e-5)

# K-Fold Cross Validation

#-------------------------------------------------------------------------------------------------------------------------------#   
# The code for preparing and performing the K-fold validation is adapted from:                                              	#
# https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-use-k-fold-cross-validation-with-keras.md 	#
#                                                                                                                           	#
# To Make this clear, the author of the report has mostly used the same variable names and format so the examiner can       	#
# distinguish between the adaptations and the cited resource above.                                                         	#
#-------------------------------------------------------------------------------------------------------------------------------#


"""
  Print the Folds Shape and Class Balance of a designated fold (1 in this circumstance)
  @k_train - The train data about to be trained on
  @k_test - The test data about to be trained on
"""

def print_fold_information(k_train, k_test_labels, k_train_labels) :
  print("-----------------------------------------------")
  print("Shapes of the train and test data for fold 1")
  print("-----------------------------------------------")
  print(f'> Fold 1 train shape {k_train.shape}')
  print(f'> Fold 1 test shape {k_test_labels.shape}')
  print("-----------------------------------------------")
  print("Display the class balance for fold 1")
  print("-----------------------------------------------")
  # Display Class Balance in the k_data
  test = Counter(k_test_labels.flatten())
  train = Counter(k_train_labels.flatten())
  plot_bar_for_balance_metrics(sorted(test.items()), "Fold 1 Test Class Balance")
  plot_bar_for_balance_metrics(sorted(train.items()), "Fold 1 Test Class Balance")
  return

kfold = KFold(n_splits=split_num, shuffle=isShuffled)



# Merge the x_train, x_test and y_train, and y_test for cross validation
input_train = np.concatenate((x_train, x_test), axis=0)
input_test = np.concatenate((y_train, y_test), axis=0)

"""
  !! ISSUES WITH INDENTATION WHEN COPYING FROM WORD/PDF DOCUMENT TO CODE FILE 
  PLEASE SEE APPENDIX B FOR A SCREEN SHOT OF THE FORMATTING !!

  Reusable Method to perform k fold validation on a designated model
  @model_to_validate - The model to implement k-fold cross validation on
  @epoch_num - The number of epochs for fitting the model
  @optimizer - The optimizer to use during the fit process
  @batch_num - The batch size when fitting the model
"""

def k_fold_validation(model_to_validate, epoch_number, optimizer, batch_num) :
  # Per-fold Store container
  acc_per_fold = []
  loss_per_fold = []
  # Begin Cross Validation
  fold_no = 1
  for train, test in kfold.split(input_train, input_test) :
	# Print fold information on the first fold
	if fold_no == 1 :
  	print_fold_information(input_train[train], input_test[test], input_test[train])
	# Instantiate the Final Model
	model = model_to_validate()
	# Compile Using the Hyper Parameters
	model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=metrics_arr)
	# One-hot encode the training parameters
	train_one_hot = keras.utils.to_categorical(input_test[train], 10)
	test_one_hot = keras.utils.to_categorical(input_test[test], 10)
	# Ouput Fold information, Fit the model and Evaluate it
	print('------------------------------------------------------------------------')
	print(f'Fold {fold_no}')
	print('------------------------------------------------------------------------')
	hist = model.fit(input_train[train], train_one_hot, verbose=1, batch_size=batch_num, epochs=epoch_number)
	print('------------------------------------------------------------------------')
	print(f'Testing for {fold_no}')
	evaluation = model.evaluate(input_train[test], test_one_hot, verbose=1)
    	# Ouput final Score for the model
	print('------------------------------------------------------------------------')
	print(f'Evaluation Metrics for fold {fold_no}: ')
	print(f'> Evaluation {model.metrics_names[0]}: {evaluation[0]}' )
	print(f'> Evaluation {model.metrics_names[1]}: {evaluation[1]}%' )
	# Append Evaluation metrics to the appropriate array for Overall Evaluation
	acc_per_fold.append(evaluation[1] * 100)
	loss_per_fold.append(evaluation[0])
	# Add one to the fold number
	fold_no = fold_no + 1

  return (acc_per_fold, loss_per_fold)



"""
  !! ISSUES WITH INDENTATION WHEN COPYING FROM WORD/PDF DOCUMENT TO CODE FILE
  PLEASE SEE APPENDIX C FOR A SCREEN SHOT OF THE FORMATTING !

  Method for printing the final metrics after k-fold validation

  @acc_per_fold = Accuracies recorded per fold for specific model
  @loss_per_fold = Loss recorded per fold for a specific model
  @title = The name of the model thats accuracies are being printed
"""

def print_k_fold_metrics(acc_per_fold, loss_per_fold, title) :
  # Performance metrics
  print('------------------------------------------------------------------------')
  print(f'Evaluation metrics per fold for model: {title}')
  # Print the metrics for Every fold
  for i in range(0, len(acc_per_fold)):
	print('------------------------------------------------------------------------')
	print(f'> Fold {i+1} - Loss: {loss_per_fold[i]} - Accuracy: {acc_per_fold[i]}%')
  #Print the Averages - Mean Accuracy, Standard Deviation and Mean loss
  print('------------------------------------------------------------------------')
  print('Average Evaluation metrics for all folds:')
  print(f'> Mean Accuracy: {np.mean(acc_per_fold)} (+- {np.std(acc_per_fold)})')
  print(f'> Mean Loss: {np.mean(loss_per_fold)}')
  print('------------------------------------------------------------------------')

(final_acc_per_fold, final_loss_per_fold) = k_fold_validation(final_model, epoch_num, sgd_final, batch_size_final)

# Print the Metrics for k-fold validation
print_k_fold_metrics(final_acc_per_fold, final_loss_per_fold)

# Instantiate All Models For Comparison:

# Baseline Model (BM)
baseline = original_model()
# Final Model (FM)
final = final_model()
# Final Model to be optimized with adam
final_adam = final_model()
# Final Model with SGD optimizer but no momentum
final_no_momentum = final_model()
# Final Model with no Batch Normalization
final_no_batch = final_model_no_batch()
# Final model with a deeper architecture
final_deep = final_model_deep()

# Compile the models with appropriate hyperparameters
baseline.compile(loss='categorical_crossentropy', optimizer='adam', metrics=metrics_arr)
final.compile(loss='categorical_crossentropy', optimizer=sgd_final, metrics=metrics_arr)
final_adam.compile(loss='categorical_crossentropy', optimizer='adam', metrics=metrics_arr)
final_no_momentum.compile(loss='categorical_crossentropy', optimizer=sgd_no_momentum, metrics=metrics_arr)
final_no_batch.compile(loss='categorical_crossentropy', optimizer=sgd_final, metrics=metrics_arr)
final_deep.compile(loss='categorical_crossentropy', optimizer=sgd_final, metrics=metrics_arr)

# Begin Training

print("======================")
print("Baseline Model BM")
print("======================")
baseline_model_hist = baseline.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_og , epochs=epoch_num_og, validation_split=validation_split_percentage, shuffle=True)
print("======================")
print("Final Model (FM) ")
print("======================")
final_model_hist = final.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_final, epochs=epoch_num, validation_split=validation_split_percentage, shuffle=True)
print("======================")
print("Final Model Adam Optimizer ")
print("======================")
final_model_adam_hist = final_adam.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_final, epochs=epoch_num, validation_split=validation_split_percentage, shuffle=True)
print("======================")
print("Final Model No Momentum ")
print("======================")
final_model_no_momentum_hist = final_no_momentum.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_final, epochs=epoch_num, validation_split=validation_split_percentage, shuffle=True)
print("======================")
print("Final Model No Batch ")
print("======================")
final_model_no_batch_hist = final_no_batch.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_final, epochs=epoch_num, validation_split=validation_split_percentage, shuffle=True)
print("======================")
print("Final Model Deeper Architecture ")
print("======================")
final_model_deep_hist = final_deep.fit(x_train, y_train_one_hot, verbose=1, batch_size=batch_size_final, epochs=epoch_num, validation_split=validation_split_percentage, shuffle=True)

# Establishing a Bed for Model Comparisons

"""
  Method for predicting all accuracy metrics (Unused in final report)

  @metric - The metric to show (e.g val_accuracy)
  @title - The title of the plot
  @y_label - The y label of the plot
"""
def compare_metrics_all_models(metric, title, y_label) :  
  plt.plot(baseline_model_hist.history[metric])
  plt.plot(final_model_hist.history[metric])
  plt.plot(final_model_adam_hist.history[metric])
  plt.plot(final_model_no_momentum_hist.history[metric])
  plt.plot(final_model_no_batch_hist.history[metric])
  plt.plot(final_model_deep_hist.history[metric])
  plt.title(title)
  plt.ylabel(y_label)
  plt.xlabel("Epoch")
  plt.legend(['Baseline Model', "LeNet5 Model", "Final Model", "Final Model w/Adam optimizer", "Final Model (no momentum)", "Final Model (No Batch Normalization)", "Final Model (Deeper Architecture)"], loc="lower right")
  plt.show()

"""
  Method for showing accuracy metrics across a particular models training history

  @hist - The history to show (e.g val_accuracy)
  @title - The title
"""
def print_acc_metrics (hist, title):
  plt.plot(hist.history['accuracy'])
  plt.plot(hist.history['val_accuracy'])
  plt.title(title)
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(['train acc', 'val acc'], loc="lower right")
  plt.show()

"""
  Method for prediction loss metrics for a particular models training history

  @hist - The history to show
  @title - The title
"""

def print_loss_metrics (hist, title):
  plt.plot(hist.history['loss'])
  plt.plot(hist.history['val_loss'])
  plt.title(title)
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(['train acc', 'val acc'], loc="upper right")
  plt.show()

"""
  Compare Loss Metrics between two designated model

  @hist1, @hist2 - Models to show
  @title - Title of the graph
  @labels - Labels for the legend
"""

def compare_loss_metrics(hist1, hist2, title, labels) :
  plt.plot(hist1.history['val_loss'])
  plt.plot(hist2.history['val_loss'])
  plt.title(title)
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(labels, loc="upper right")
  plt.show()

"""
  Compare Validation Accuracy Metrics between two designated model

  @hist1, @hist2 - Models to show
  @title - Title of the graph
  @labels - Labels for the legend
"""

def compare_acc_metrics(hist1, hist2, title, labels) :
  plt.plot(hist1.history['val_accuracy'])
  plt.plot(hist2.history['val_accuracy'])
  plt.title(title)
  plt.ylabel('accuracy')
  plt.xlabel('Epoch')
  plt.legend(labels, loc="lower right")
  plt.show()


"""
  plot a confusion matrix given a set of predictions

  @hist1, @hist2 - Models to show
  @title - Title of the graph
  @labels - Labels for the legend
"""

def plot_confusion_matrix(cm_predictions) :
  confusion = confusion_matrix(y_test, cm_predictions)
  plt.figure(figsize=(10, 10))
  sns.heatmap(confusion, annot=True, cbar=False, fmt='g', xticklabels=class_names, yticklabels=class_names)

# Baseline vs Original Model Comparisons

# Show Individual Accuracy and Loss Metrics (FM vs BM)
print_acc_metrics(baseline_model_hist, "Baseline Model Accuracy")
print_acc_metrics(final_model_hist, "Final Model Accuracy")
print_loss_metrics(baseline_model_hist, "Baseline Model Loss")
print_loss_metrics(final_model_hist, "Final Model Loss")

# Compare Validation accuracy and validation loss metrics (FM vs BM)
compare_loss_metrics(final_model_hist, baseline_model_hist, "Final Model (FM) vs Baseline Model (BM) - Validation Loss", ['Final Model (FM)', "Baseline Model (BM)"])
compare_acc_metrics(final_model_hist, baseline_model_hist, "Final Model (FM) vs Baseline Model (BM) - Validation Accuracy", ['Final Model (FM)', "Baseline Model (BM)"])

# Evaluate the FM and the BM
print("----------------------------------------")
print("Evaluation of the FM on unseen data")
print("----------------------------------------")
final_predictions = final.evaluate(x_test, y_test_one_hot, return_dict=True)
print("----------------------------------------")
print("Evaluation of the BM on unseen data")
print("----------------------------------------")
baseline_predictions = baseline.evaluate(x_test, y_test_one_hot, return_dict=True)
print("----------------------------------------")

# BM vs FM breakdown of statistics
df = pd.DataFrame()
df['pred_acc'] = [f"{round(final_predictions['accuracy'], 2)}", f"{round(baseline_predictions['accuracy'], 2)}"]
df['pred_loss'] = [f"{round(final_predictions['loss'], 2)}", f"{round(baseline_predictions['loss'], 2)}"]
df['train_acc'] = [f"{round(final_model_hist.history['accuracy'][-1], 2)}", f"{round(baseline_model_hist.history['accuracy'][-1], 2)}"]
df['train_loss'] = [f"{round(final_model_hist.history['loss'][-1], 2)}", f"{round(baseline_model_hist.history['loss'][-1], 2)}"]
df.columns = ['Evaluation Accuracy', 'Evaluation Loss', 'Train Accuracy', 'Train Loss']
df.index = ['Final Model (FM)', 'Baseline Model (BM)']
df.head()

# Final Model further Analysis

# Establish Class Names
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

# Use predict data for plotting performance metrics
pred = final.predict(x_test)

# Plot Confusion Matrix
cm_predictions = pred.argmax(axis=1)
plot_confusion_matrix(cm_predictions)

# Plot Recall, F1, Precision Scores
print(classification_report(cm_predictions, y_test))

# Experimental Model Comparisons

# Compare all Validation accuracy and Loss Results

# Print Accuracy Metrics
print_acc_metrics(final_model_adam_hist, "Final Model (Adam Optimizer)")
print_acc_metrics(final_model_no_momentum_hist, "Final Model (No Momentum)")
print_acc_metrics(final_model_no_batch_hist, "Final Model (No Batch Normalization)")
print_acc_metrics(final_model_deep_hist, "Final Model (No Batch Normalization)")

# Print Loss Metrics
print_loss_metrics(final_model_adam_hist, "Final Model (Adam Optimizer)")
print_loss_metrics(final_model_no_momentum_hist, "Final Model (No Momentum)")
print_loss_metrics(final_model_no_batch_hist, "Final Model (No Batch Normalization)")
print_loss_metrics(final_model_deep_hist, "Final Model (No Batch Normalization)")

# Compare Metrics Adam vs SGD
compare_loss_metrics(final_model_hist, final_model_adam_hist, "FM (SGD) vs FM (Adam) - val_loss", ['Final Model (with SGD)', "Final Model (with adam)"])
compare_acc_metrics(final_model_hist, final_model_adam_hist, "FM (SGD) vs FM (Adam) - val_acc", ['Final Model (with SGD)', "Final Model (with adam)"])

# Compare Metrics Momentum vs No Momentum
compare_loss_metrics(final_model_hist, final_model_no_momentum_hist, "FM w/Momentum vs FM wo/momentum - val_loss", ['Final Model (with momentum)', "Final Model (without momentum)"])
compare_acc_metrics(final_model_hist, final_model_no_momentum_hist, "FM w/Momentum vs FM wo/momentum - val_acc", ['Final Model (with momentum)', "Final Model (without momentum)"])

# Compare Metrics Batch Normalization vs No Batch Normalization
compare_loss_metrics(final_model_hist, final_model_no_batch_hist, "FM vs FM (No Batch Normalization) - loss", ['Final Model', "Final Model (without Batch Normalization)"])
compare_acc_metrics(final_model_hist, final_model_no_batch_hist, "FM vs FM (No Batch Normalization) - acc", ['Final Model', "Final Model (without Batch Normalization)"])

# Compare Final Model vs Deeper Model (Omitted from final report)
compare_loss_metrics(final_model_hist, final_model_deep_hist, "FM vs Deeper Architecture  - val_loss", ['Final Model', "Deeper Architecture"])
compare_acc_metrics(final_model_hist, final_model_deep_hist, "FM vs Deeper Architecture - val_acc", ['Final Model', "Deeper Architecture"])

# Save the FM
final.save("final_model_W21045778.h5")
