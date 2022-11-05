# What does each layer learn in CNNs?

A modern CNN consists of multiple layers for learning from simple to increasingly more abstract features for object recognition.
The following will look at the common types of features computed bby different layers: 

## Convolutional Layer 1: Edges and Blobs

The first layer will look for simple edges an blobs from an input image. 

These features arise because a low-level convolutional kernal (for example 3x3) can respond strongly to gradient changes on the raw input image. They often convey simple bbut useful structural information. 

##  Convolutional Layer 3: Texture

After a few convolutional layers the network will start to extract more complex patterns of the input. 
This is done by combining low level and blob features.

The textures capture more structures of the input and occupy a larger spatial support than the edges and blobbs 

## Convolutional Layer 5: Object parts 

More abstract object part features start to emerge on this layer.
When When incoming texture features are convoluted for a few more layers, they can be further processed and configured by the network to form increasingly more meaningful patterns that appear frequently among images of certain categories. 

## Fully Connected Layers: Object Classification and Classes 

For the sake of object recognition, object part features are flattened and transformed by a few fully connected layers, which can be trained to retain featuyres sufficiently discriminative for classifying images into distinct categories. 

The final output would be a vector of predicted probabilites for different classes. 

### Python code 

You can view the python code for a CNN in the code folder entitled CNN.py