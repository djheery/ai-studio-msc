# General Learning Process in MLP 

The learning process in Multi-Layered Perceptrons can be generally organised as: 

1. Compute the outputs 
2. Compare outputs with desired targets 
3. Adjust the weights and repeat the process 

## Backpropagation for Neural Network Training 

There is a good diagram in the course section that matches this filename: 

Steps for bbackpropagation: 

1. Initialize the weights 
2. Read the input vector and desired output 
3. Compute the actual output via the calculations 
4. Compute the error 
5. Change the weights by working backwards using the backpropagation alogorithm 
6. Repat the process for all examples in your training data. 
  - Round one of updating the network for the entire training dataset is called an **epoch**
  - A network may be trained for tens, hundreds or many thousands of epochs. 

## Prediction 

Once the training process of an ANN is completed you can then use it to make predictions. 
This is done on the validation dataset, which as named validates that your model performs as expected on unseen data.

If the obtained results are satisfactory, you can deploy it operationally and use it to make predictions continuously. 

The network architecture and the final set of weights are the parameters that youi need to save from the model.
Predictions are made by providing the input to the neural network and performing a forward-pass allowing it to generate an output that you can use as a prediction. 

## Universal Approximation

A linear combination of 'enough' sigmoids can approximate any smooth functions with any degree of accuracy. 
A single hidden layer can be adequation 

- This is true in theory
- In the implementation, you may end up with an infinite number of hidden neurons which is not practical.
- Recent research shows that when using a finite number of neurons, more hidden layers achieve better results. 
  - This leads to multilayer neural networks such as the multilayer perceptron (MLP) and CNN which will be covered later. 

## Designing a neural Network to 'Detect' A digit

Hypethetically you can use apnel made up of an 8x8 grid with each cell either being on or off.
You want your neural net ot let you know whenever it thinks it sees the character '4'.
This is serialized into (8*8) which is equal to 64 cells. 

- Architecture: 
  - The nerual network will have 64 inputs
    - Each input represents a particular cell in the panel
  - A hidden layer consists of a number of neurons all feeding their output into just one neuron in the output layer as it is a binary classification task. 
- Activation function: 
  - Sigmoid

You can view the code in the code folder and the file entitled MLP.py

## MLP Sumamry: 

MLPs are useful for their ability to solve problems related to regression and classification.

MLPs are universal function approximators as shown by Cybenko's (1989) theorem. As classification is a particular case of regression when the response variable is categorical, MLPs make good classifier algorithms.

MLPs were a popular machine learning solution, finding applications in diverse fields such as speech recognition, image recognition and machine translation software, but thereafter faced strong competition from much simpler support vector machines. Interest in backpropagation networks returned due to the successes of deep learning.