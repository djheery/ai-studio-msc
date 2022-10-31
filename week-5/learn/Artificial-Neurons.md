# How do we actually 'use' an artificial neuron 

The module starts with asking the question of the reader, how do you use an artificial neuron? 

My answer: 

Artificial neurons are used via code implementation. They offer a method of learning through repetition over a labeled data set, each time assessing how "correct" their output was, and adjusting the weights in the network to fit the labeled data. 

Given answer: 

You create layers of neurons. The neurons in each layer feed their output forward to the next layer until you get the final output of a ANN. 

## Artificial Neurons 

The neural network has dominated the applications of AI since its inception in the 1980s. 
The most elementary form of an ANN is a neuron. 

An artificial neuron can have n inputs.
Each input will have a corresponding weight w. 

Each input is fed into the a node in the next hidden layer. 
There can be n hidden layers. 

The summation of (i[n] * w[n] + b) is passed into that node on the hidden layer and this feeds forward until the output.  

## General Architecture of a Multi Layer Perceptron (MLP)

A multilayer perceptron (MLP) is formuated from loose biological principles. 
It learns from the given data. 

It is a non-linear model that has a layered, feed-forward structure. 

The General Structure is as follows: 

1. Input or Visible Layers 
2. Hidden Layers 
3. Output Layer 

### Input or Visible Layers

The first layer is named the input layer. This is because it takes the input of the provided data. 
This and the output layer are generally the only exposed parts of the network. 

They are often drawn like neurons, but they are not. They are there to pass through to the next layer. 

### Hidden Layers

Layers after the input layer are called hidden layers. 
Deep learning refers to the concept of having many hidden layers in a Neural Network. 
Each neuron in a hidden layer has an associated activation function such as Sigmoind or Rectifield Linear Units (ReLU)

These layers will then feed forward to the neurons on the next layer in the same way the input layer does to this neuron. By summing the neurons on the layer with their weights and bais' 

## Output Layer 

The output layer of an ANN 