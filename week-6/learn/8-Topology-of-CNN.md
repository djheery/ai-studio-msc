# Topology of a CNN 

In a CNN there are three key steps: 

1. Convolution 
2. Activation
3. Subsampling 

The former towo steps deal with extracting non-linear features, The latter enforces some degree of invariance on the features while reducing the image dimensions. 

There is a diagram that represents each layer of a convolutional network. 

Input => 
  Feature Extraction Layer (Convolution + Activation) => 
    Subsampling Lyaer (Shift and distortion invariance) =>
      Convolution + Activation => 
        Subsampling => 
          Classification (MLP, SVM)

## The Convolutional Layer 

In a CNN, the convolution layers detect the same features at different locations in the input image. 
Convolution kernels are applied to different patches of the image rather than the entire image. 
With different levels of the convolutions, lower and lower-level features are extracted such as edges and corners and/or high level features such as objects and corners. 

## Activation Function 

The function of activation is to enhance non-linearity in the extracted features.
There is an example in this slide that demonstrates how the activation function attenuates any feature with a less than zero value while maintaining any positive values. 

This means that the contrast between features is enhanced. 

## Common function Activations in CNN architecturesa

There are many non-linear functions used to squash the input features in various ways. 

The sigmod function, for example, continuously maps any input into the range of (0, 1).
The output range of the tanh functin is (-1, 1).
The ReLU truncates any negative part of any input to zeros.
Leaky ReLU alows negatives within a given bound.

common Functions: 

- Sigmoid
- Tanh
- ReLU
- Leaky ReLU
- ELU 

## Sub Sampling: 

Subsampling layers are also known as pooling layers.
They are usded to reduce the spactial dimensions of feature maps.
This can introduce som invariance for learned features. 

It can reduce the computational workload of a CNN model considerably and produce more discrimanative features.
A common pooling operation is called max pooling which simply keeps the maximum value within a spacial neighbourhood: 

[
  [1],[2],[4],[6],
  [8],[3],[7],[1],
  [4],[3],[1],[1],
  [7],[2],[2],[1],
]

A Max pool with 2x2 filters with a stride of 2 (convulse of 2) will be divided like this: 

[
  [1],[2] || [4],[6]
  [8],[3] || [7],[1]
  ------------------
  [4],[3] || [1],[1]
  [7],[2] || [2],[1]
]

This would create the following 2x2 representation (remembber it keeps the max from each section):

[
  [8], [7],
  [7], [1]
]


