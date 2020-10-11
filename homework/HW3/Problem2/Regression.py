import numpy as np


# Base Regression class
class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        self.params.update(kwargs)

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError


# OLS Linear Regression class
class LinearRegression(Regression):

    def fit(self, X, y):
        n, p = X.shape
        # Append a columns of ones
        X1 = np.append(np.ones((n, 1)), X, axis=1)
        beta_hat = np.linalg.pinv(X1.T @ X1) @ X1.T @ y
        self.params['intercept'] = beta_hat[0]
        self.params['coefficients'] = beta_hat[1:]

    def predict(self, X):
        n, p = X.shape
        y_pred = X @ self.params['coefficients'] + self.params['intercept'] * np.ones(n)
        return y_pred

    def score(self, X, y):
        y_pred = self.predict(X)
        sst = np.sum((y - np.mean(y)) ** 2)
        sse = np.sum((y - y_pred) ** 2)
        r2 = 1 - float(sse) / sst
        return r2


# Ridge Regression class
class RidgeRegression(LinearRegression):

    def fit(self, X, y):
        n, p = X.shape
        # Append a columns of ones
        X1 = np.append(np.ones((n, 1)), X, axis=1)
        Gamma = self.params['alpha'] * np.eye(p+1)
        beta_hat = np.linalg.pinv(X1.T @ X1 + Gamma.T @ Gamma) @ X1.T @ y
        self.params['intercept'] = beta_hat[0]
        self.params['coefficients'] = beta_hat[1:]