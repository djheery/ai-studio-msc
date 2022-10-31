# K-Means 

K-Means is a partial clustering algorithm. 
The K-Means algortithm partitions the data into K clusters specified by the programmer. 
Each cluster has a centre called the centroid.

Clustering is a technique for finding similarities in groups of data, called clusters. 
This works by grouping data into instances that are similar to each other.
Each cluster and data instances can have very different attributes. 

Despite it's weaknesses, k-means is still the most popular algorithm due to its simplicity and efficiency. 

## K-Means process 

- First the algorithm requires the programmer to specify k data points as the initial seeds.
  - To obtain good clustering results, these seeds need to be randomly chosen. And then, the algoithm iteratively updates the cluster membership by assigning each data point to its nearest cluster centre, based on a pre-defined distance or similarity function. 
- Then the location of each centroid is updated by taking the average of locations of the data points in the corresponding cluster. #
  - This is done interatvely until some convergence criterion is met. 

## K-Means Stopping/ Convergence Criterion

The K-Means algorithm will terminate when it finds minimal change of the cluster membership of the data-points from the previous iteration. 
Sometimes the change of the location of the centroids can also be used to detect convergence, since a minimal change of centroids would imply that the cluster membership of data points would remain almost the same. 

## Strengths and Weaknesses of K-Means

K-Means is easy to implement and runs efficiently without supervision, hence qualifying for processing large amounts of data such as product reviews. However, it requires the specification of the numbber of clusters in advance and is sensitive to data outliers. This can mean that is limited when the data is noisy. 

## Strengths 

- Simple 
  - Easy to understand and implement 
- Efficient 
  - Time complexity O(tkn)
    - n: The number of datapoints 
    - k: Number of clusters 
    - t: Number of iterations
  - Since bboth k and t are small, k-means is considered a linear algorithm. 
- Popular 
  - K-means is the most popular algorithm. 

## Weaknesses

- Specification 
  - User needs to specify k 
- Sensitivity 
  - The algorithm is sensitive to outliers. 


## Handling K-Means Weaknesses

Outliers are data points that are distant from all other data-points and thus cannot be correctly clustered. 

One process of handling this sensitivity is to remove these outlier datapoints 
It is worth monitoring these possible outliers over a few iterations and decide whether removing them would help better clustering of data 

Another method is to perform random sampling. 
Sincin in sampling you only choose a small subset of data points, the chance of selecting an outlier is very small. 
Assing the rest of the data points to the clusters by distance, similiarity comparison or classification. 

The first iteration of the k-means algorithm depens on the selection of k initial seeds. As a result, different seeds c an lead to widly different clustering results, some of which are good, while others unsatisfactory. 

The algorithm is sensitive to initial seeds. 
You should use different seeds to assess which ones lead to the most effective results 



