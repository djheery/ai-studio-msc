# Undefit and Overfit Model. 

3 situations could happen with an ML model: 

1. Underfit 
2. Just Right Fit 
3. Overfit 

In the case of regression, a linear model would underfit whereas an 'overpowerful' nonlinear model would overfit the green curve. 
The just right model lies between the two extreme models. 

For example if there is an S shaped wave to the datapoints when plotted to a graph. 

A linear model would draw a straight line through (Underfit)
A just-right model would match the curve visibly, maybe to 100% accurate but visibly notice the trend of the data (just right fit)
An overpowerful model would be too sensitive too noise and may come out with steep up and down plots depending on the data (overfit)

## How do you detect this? 

Look at the error plot. In the case of underfit, the error from the training and validation curves remains high. 
In the case of overfit, the training curve has a low error, but the validation curve has a high error. 
The just-right fit results in a low error on both the training and validation. 

There are some good diagrams on this lecture slide. 