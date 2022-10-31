import numpy as np

from sklearn.decomposition import PCA

X = np.array([
  [-1, -1], [-2, -1], [-3, -2],
  [1, 1], [2, 1], [3, 2]
])

pca = PCA(n_components=2).fit(X)

print(pca.explained_variance_ratio_)

>>> [0.9924... , 0.0075...]