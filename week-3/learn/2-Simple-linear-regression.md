# Simple Linear Regression 

Regression attempts are used to model the relationship between two variables by fitting an equation to the observed data. 
Linear regression aims to fit a linear equation to the observed data. 

To obtain the linear equation you must minimise the sum of squared errors. 
This means the distance between the equation itself and the data. 

A line is determined by two parameters: 

- Slope 
- Intercept 

The slope (m) determines whether the line is upward or downward trending (positive or negative)
The intecept (c) dictates the absolute 'height' of the line on the y-axis. 

The intercept is often reffered to as the "bias" in machine learning

Where: 

Y = Output 
X = Input
m = slope 
c = intercept

The equation for a simple linear regression model is: 

Y = mX + c

## Fit the Line Using Least Squares 

To find the combination of the slope and intercept parameters for a regression model, you need to compare the model predictions with the true measurements and compute a sum of the squares of the residuals. By minimising this sum with respect to the unknown parameters, you will be able to identify a good fit of the given data. 

This method is referred to as least squares (LS) and can be applied to multiple regression and non-linear models as well. 

(There is a good diagram shown in the lectures)

## Python Code: 

View the python code in least_squares.py in the code folder.

