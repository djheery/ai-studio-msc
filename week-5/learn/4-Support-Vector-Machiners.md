# Support Vector Machines (SVM)

SVM was invented by Vladimir Vapnik and his co-workers in the 1970s in Russia. 
It became known to the west in 1992. 

SVM is a type of linear classifier that finds a hyperplane on which it can sparate two calsses of data, positive and negative. 

SVM not only has rigorous theoretical foundation but also performs classification more accurately than most other methods in application, especially for high-dimensional data. 

## Linear Classifiers

How would you classify a straight line? 

This is one example of a straight line that separates the +1 from the -1 samples.

This line is given by: 

f(x, w, b) = sign(w * x + b)

For a data point above the line (that is, w * x + b > 0), these points will be classified as +1 
For a data point that is below the line (that is, w * x + b < 0) These points will be classified as -1 

## Maximum Margin 

The margin of a linear classifier is defined as the width that the boundary could be increase by before hitting a data pint. 
This would be possible after maximising margin becasue it introduces robustness to the model. 

It imples that only support vectors are important, other training examples are ignorable emperically.
In practice it works very well 

**Linear SVM** = This is a linear classifier with maximum margin. The simplest kind of SVM. 
**Support Vectors** = The data points that the margin pushes up again. 

## What happens if a classifier has a small margin? 

You want a classifier with the maximum margin as you increase the classifiers margin of/ tolerance against error

## Nonlinear SVM 

Datasets that are linearly separble work well with linear SVM. 
As you can see, the red and blue datapints are clearly sparated by a straight line. The support vetors are shown in circles in the diagram on this page. 

When data is not linearly seperable SVM maps the data to a higher dimensional space. 

When another dimension is added it creates more space between data points allowing them to become seperable.
This is done in a diagram on this module section by adding an extra dimension in this case a y axis by squaring x. 

## Feature Spaces 

The strength of SVM is that it has rigourous theoretical foundation. 
Due to this it can perform classification more accurately than other ML methods. 
It is expecially effective in high dimensional data. 

An example: 

x1, x2, x3, and x4 are inputs to the SVM. 

The dimensionality of the input is 4. 

SVM finds a hyperplane on which tow classes of data are seperable, positive and negative. 

The linear classifier tries to find a seperating line that maximizes the margin between the support vectors. 

Kernel functions are used for nonlinear separation, these become 'none-linear SVMs' 

The role of these kernal functions is to transform the data to a higher dimensional space also known as the feature space where the data becomes seperable. 

### Nonlinear SVMs: Feature Spaces

General idea: the original input space can always be mapped to some higher dimensional feature space where the training set is separable.

There is a diagram on this section that shows that by mapping datapoints to a higher dimensions reveal ways in which the datapoints become seperable via use of kernel functions which are responsible for mapping the dataset to the higher dimensional space.

### Kernel Functions

In nonlinear SVM, kernal functions are used to perform the high dimensional transformation.

The most common kerners are: 

- Linear 
- Polynomial (Power or p)
- Gaussian (Radial-bias function network)
- Sigmoid

You need to specify the kernel when running SVM. 

You can view an example of the code in ./code/svm.py