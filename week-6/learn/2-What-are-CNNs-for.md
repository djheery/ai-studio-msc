# What are Convolutional Networks For? 

This slide asks me to reflect on what you already know about multilayer perceptrons and Neural Networks:  

MultiLayer perceptrons are computational pathways consiting of layers: 

- Input Layer 
- Hidden Layer 
- Output Layer 

The input layer consists of inputs/ different data features. 
Weights and Bias' are then attached to the connections between each layer and each neuron on the hidden layer computes a weighted sum of all neurons/inputs on the prior layer. 

The neurons in the hidden layer then perfom some kind of activation function, maybe ReLU or Sigmoid and pass this information to the next hidden layer or finally to the output. 

If the next layer is a hidden layer, the weighted sum of all neurons on the prior layer will be fed forward again and then passed into another activation function and so on. 

When the output layer is reached, in the training stage, this output will be validated against the datas label. 

Outputs can be: 

- Singular 
- Binary 
- Multi-Class 

An error function calculates the error margin of the output produced by the neural network. If this error is high i.e. it has read to an innacurate output, then the weights in the ANN will be updated layer by layer, backwards through network until the first hidden layer the input layer is reached. This is a process called backpropagation and will continue until the desired output and actual output converge. 

The core concept of Neural Networks is to make the pathways long so the encourage complexity. This complexity becomes able to represent very abstract relationships which eventually lead to a desired output. This desired output can be correct class classification, true or false or singular value. 

Convolutional Neural Networks are a type of neural network that take images as input. 
Each input node corresponds to some different part of an image. 

In each hidden layer filters will be applied to the image slice via kernel convolution, each filter trying to highlight some unique feature of an image. These kernel filters will identify more and more abstract features as time goes on. 

These Convolutional Layers are generally followed by a Dense layer for classification purposes. 

## Given Information about CNNs 

The inherent design of the CNN makes it well-suite for computer vision and image processing operations, such as object recognition, image recognition and gesture recognition.

This technology proves to be a great improvement over traditional fully connected neural networks, while providing a degree of robustness to distortions in input images. 

