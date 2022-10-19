# Logistic Regression 

Logistic Regression is a statistical method for predicting binary classes, therefore in its bbasic form uses logistic function to model a binary dependent variable. 

The outocme or target is dichotomous in nature. Dichotmous means that there are only two possible classes. 

For example, it can be used for cancer detection problems. 
It computes the probability of an event occurrence. 

The key difference between linear regression and logistic regression is that the former outputs continuous values of both positive and negative, while the latter only outputs values between 0 and 1. 

These values represent estimated probabilites of the corresponding event. 

Each event being detected would be assigned a probability between 0 and 1, with a sum of one. 

## Why can't I use Linear Regression for Classification? 

Linear regression slopes can be much larger than 1 or much smaller than 0 and hence thresholding becomes difficult. 
The actual class values are 0 and 1, whereas linear regression gives continuous values in the entire erange. 

This is the reason you cannot directly use linear regression for classification problems. 
However with a little extension and using a sigmoid function, you can transform linear regression to solve a classification problem. 

This is known as logistic regression. 

Logistic regression equation: 

        1
    ____________
    1+e**-(mX+c)

## Logistic Function (S-Curve)

The logistic function (also known as the s-curve) is used to model the probability of a certain class or event existing. 
These could be classes such as win/lose, die/live, healthy/sick 

The output of a logistic function is mathematically garunteed to be between 0 and 1, representing the estimated probability of a certain event as previously described. 

lThere is a good diagram in the learn slide of this entitled sub section. 

