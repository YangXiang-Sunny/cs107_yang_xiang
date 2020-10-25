from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression as LR
from Regression import RidgeRegression as RR

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np


X, y = datasets.load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model1 = LR()
model2 = RR()

model3 = LinearRegression()
model4 = Ridge(alpha=0.01, fit_intercept=True)

alphas = np.linspace(0.1, 50, 1)
score_model3 = []
score_model4 = []

for alpha in alphas:
    model4 = Ridge(alpha=alpha, fit_intercept=True)
    # Fit model on training data
    model3.fit(X_train, y_train)
    model4.fit(X_train, y_train)
    # Calculate score on test data
    score_model3.append(r2_score(y_test, model3.predict(X_test)))
    score_model4.append(r2_score(y_test, model4.predict(X_test)))

# Plot alpha vs score
plt.figure(figsize=(8, 8))
plt.plot(alphas, score_model3, label='Linear Regression')
plt.plot(alphas, score_model4, label='Ridge Regression')
plt.legend()
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('R2 score')
plt.title('Model Performance')
plt.show()

# model2.set_params(alpha=0.1)
# models = [model1, model2, model3, model4]
#
# print(X_train.shape, y_train.shape)
# for model in models:
#     model.fit(X_train, y_train)
#
# r2_model1 = model1.score(X_test, y_test)
# r2_model2 = model2.score(X_test, y_test)
# r2_model3 = r2_score(y_test, model3.predict(X_test))
# r2_model4 = r2_score(y_test, model4.predict(X_test))
# print(r2_model1, r2_model2, r2_model3, r2_model4)
#
# if r2_model1 > r2_model2:
#     print('Linear Regression is better, and its parameters are ', model1.get_params())
# else:
#     print('Ridge Regression is better, and its parameters are ', model2.get_params())