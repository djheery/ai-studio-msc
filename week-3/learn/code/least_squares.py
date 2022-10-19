import numpy as nump 
from sklearn.linear_model import LinearRegression

# Model (Bi-variate): y = 1 * x_0 + 2 * x_1 + 3

X = np.array([[1, 1],[1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.coef_ 
reg.intercept_ 
reg.predict(np.array([[3, 5]]))