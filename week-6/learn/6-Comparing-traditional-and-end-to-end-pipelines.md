# Comparing Traditional and End-to-End pipelines

This slide looks at the difference between traditional and end-to-end piplines. 

## Traditional Pipelines 

Traditional pipelines are as follows: 

- Input 
  - Pre-processing for feature extraction (For example, PCA, NMF)
    - Feature 
      - Classification 
        - Output 

Traditional methods reqiuire a pre-processing step for feature extraction. This is manual feature engineering which cannot take into account all invariants (for instance, scale, location orientation).

This means that it cannot be jointly optimized with the subsequent classification model. 

## End-To-End Learning Pipelines 

Modern Deep Learning (such as CNNs) intergrate feature extraction and classification so that inputs can directly be mapped to outputs. 
The end-to-end joint optimization of both modules can learn more powerful features and embed stronger invariances for pattern recognition.

It looks like this: 

- Input 
  - [Feature Extraction => Shift and Distortion Invariance => Classification]
    - Output

 