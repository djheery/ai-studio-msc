# Non-Neagative Matrix Factorisation

Non-negative matrix factorisation (NMF) is a group of algorithms in machine learning where a matrix V is factorised into two matrices W and H, with the property that all three matricis have no negative elements 

The matrices W and H are estimated to be as 'close' as possible to the initial observation matrix V. 

To measure the accuracy, you use the Euclidean distance metric between V and W · H

## Observation Data Matrix

This is th ematrix of data points to be decomposed into components. 
It serves as the supervision signal for the NMF algorithm to reconstruct from the identified W and H components. 
The accuracy of the reconstruction is measured using the Eclidean distance between V and W · H 

## W 

**Patterns**

This is the matrix of data patterns to be solved by the NMF algorithm. It has the same number of rows as the data matrix but usually contains much fewer columns which can be interpreted as the main patterns or components that can be combined to explain each row of the data matrix. 

Some examples of this can be 'expanatory variables, 'basis' and dictionary 

## H

**Activation Coefficients**

This is the matrix of activation coefficients to be optimised along with the matrix W by the NMF algorithm. 

The matrix H has the same numbber of rows as W and the same number of columns. This means that each column of the matrix is responsible for reconstructing the corresponding colum of the data matrix bby linearly combining the patterns of W using the activation coefficients. 
