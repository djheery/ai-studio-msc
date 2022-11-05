# Putting the Blocks together: LeNet5

There is a diagram of the resnet on this slide:

The architectual detail of LeNet5 CNN (shown in said diagram) are: 

- Raw Image of 32x32 pixels
- C1, C3, C5: Convolutional Layer
- 5x5 Convolution Matrix
- Activation Function: ReLU or tanh
- S2, S4: Subsampling
- Subsampling by a factor of 2
- F6 Fully conntected Layer:

The Architeure is as follows: 

Input => (convolutions) => 
  C1: Feature Maps (6@28x28) => (subsampling) =>
    S2: feature map (6@14x14) => (convolutions) => 
      C3: (16@10x10) => (subsampling) => 
        S4: (16@5x5) => (full connection/ Convolutional Layer)
          C5: layer (120@) => (Full connection)
            F6: layer (84@) => (output) => 
              Output (@10) Gaussian Connections
          
@ = the amount of neurons in a layer precceeds the @

