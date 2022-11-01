# Performance Evaluation

This section introduces the concept of evaluating ANN, especially in the case of classifications. 
This allows you to understand the efficiency of the ANN classifiers so that they can be compared with each other. 

You will start with te concept of validation and then the different performace metrics for classification. 

## K-Fold Cross Validation

For a k-fold cross-validation, you should start dividing your training set into k parts. 
Each iteration you pick (k-1) parts for training and pick the rest of the parts for testing, and then measure the performance. 

To consider, average the performance from those K iterations. There is less bais, but this is computationally intensive (train K * d times)

## Performance Metrics for Classification 

For a performance metrics for classification, you may consider the confusion matrix which captures all the information about a classifier performance, but is not scalar. 

### Confusion matrix propertios 

- Total sum is fixed (population)
- Colum sums are fixed (class-wise population)
- Wuality of model and selected threshold decide how columns are split into rows 
- You want diagonals to be 'heavy,off diagonals to be light

For example: 

True Positive   |   False Positive
                |   
    9           |     2
                |
====================================
                |
    1           |     8
                |
False Negative      True Negative 

## Metrics 

Various definitions of classification metrics exist. 

TP = True Positive
FN = False Negative 
TN = True Negative 
FP = False Positive

Here are some common ones:

### Accuracy


What fraction of all predictions did you get right: 

Accuracy = (TP + TN) / (TP + TN + FP + FN)

### Recall (Sensitivity) 

What fraction of all greens did you pick out? 
Also known as TP rate (TPR) 

TPR = TP / (TP + FN)

### Precision 

Quality of Predictions, also called Positive Predictive Value (PPV)

PPV = TP / (TP + FP)

### Negative Recall (Specificity)

Also known as True Negative Rate (TNR)
What fraction of all negatives in the population were you able to keep away? 

TNR = TN / (TN + FP)

## F-Score

Summary of precision and recall into a single score 

Also called harmonic mean of precision and recall. 

F-Score = 2 * (Pecision * Recall) / (Precision + Recall)



