from sklearn import svm

X = [
  [0, 0],
  [1, 1]
]

y = [0, 1]

clf = svm.SVC(kernel='linear')
clf.fit(X, y)
clf.predict([[2., 2.]])

array([1])

