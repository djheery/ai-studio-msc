# Decision Tree 

A decision tree, is a tree like structure that models a decision makeing process. 
It contains conditional control statements.

A decision tree has a flowchart like structure. 

1. Each internal node represents a 'test' on an attribute 
  - One example could be "income > 20K"
2. Each branch represents the outcome of the test, and each leaf node represents a class label.
3. The paths from root to leaf represent classification rules. 

## Decision Tree Attributes 

Each internal node tests an attribute. 

Some exampels of this can be the humidity, temperature of a particular day or age, hair colour of a particular employee. 

## Decision Tree Value Nodes 

Each branch corresponds to an attribbute value node. 

Some examples could be humidity of a day, it can be normal or high. 
Another examzple is wheter a credit card applicatnts income is low, medium or high. 

The branch may also signify the applicants employment status. 

## Decision Tree Classification

Each leaf node assigns a classification. 

Some examples of this can be, whether to lend a credit card to a particular person based on results of nodes and branches of the decision tree. 
Wheter someone has cancer or not based on certain criteria. 

## Entropy and Information Gain. 

A decision tree is recursively built by choosing the best variable to split the collection of data points that fall into the current branch. 
One popular criterion of a split is that it should lead to purer subsets of samples compared with the incoming data. 

As a result, the information gain (IG) and entropy are often used to measure the purity of each split for selecting the best one. 

Entropy(S): Measures the spread of the data in training set S over the classes (+ or -)
Gain(S, A): Change in entropy before S and after A the split 

