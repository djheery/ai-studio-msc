# Principal Component Analysis 

Principal Component Analysis (PCA) is used in exploratory data analysis and for making predictive models. 

It is commonly used for dimensionality reduction by projecting each data point onto only the first few principal components to obtain lower-dimensional data while preserving as mcuh of the data's variation as possible. 

Application domains include, facial recognition, computer vision, and image compression. 

It is also used for finding patterns in data of high dimensions in the field of finance, data mining, psychology, and bioinformatics. 

## Why Dimensionality Redcuction 

PCA is commonly used for dimensionality reduction by projecting each data point onto only the first few components to obtain lower-dimensional data while preserving as much of the data's variation as possible. 

It reduces time complxity which means less computation. 
It reduces space complexity which means fewer parameters 
It saves the cost of aquiring features. 

Simpler models are more robust, easier to interpret with simpler explanations and provide data visualisation. 

## What PCA does 

Mathematically, PCA computers:

z = W[T](x - m)

W = teh eigenvectors of covarience matrix 
m = sample mean 

### What does this mean

PCA centres the data to the origin and rotates the axes. 

There is a graphic on the slide with the same name as this file. 

It is used to find the key datapoints which explain the varience in data. 

