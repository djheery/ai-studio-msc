# K-Means example 

from sklearn.cluster import KMeans 
import numpy as np 

X = np.array(
              [
                [1, 2], [1, 4], [1, 0],
                [10, 2], [10, 4], [10, 0]
              ]
            )

# Random state = Intial Seeds 
# n_clusters = number of clusters (k)

kmeans = KMeans(n_cluster=2, random_state=0).fit(X)

# Analysis 

kmeans.labels_ # Prints the data point labels
kmeans.predict([[0, 0], [12, 3]]) # Predicts the clusters of new data pints
kmeans.cluster_centers_ # Shows the cluster centers