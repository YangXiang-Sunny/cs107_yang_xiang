# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from Regression import LinearRegression as LR

model1 = LR()
model2 = LinearRegression()

X = np.array([[1, 2, 7], [2, 4, 8], [3, 5, 3], [4, 4, 4], [6, 7, 8]])
y = np.array([[0], [3], [2], [4], [5]])

model1.fit(X, y)
model2.fit(X, y)

# test fit and get_params
print(model1.get_params())
print(model2.coef_, model2.intercept_)

# test predict
print(model1.predict(X) - model2.predict(X))

# test score
print(model1.score(X, y))
print(r2_score(y, model2.predict(X)))
