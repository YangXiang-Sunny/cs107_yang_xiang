from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import Regression as Rg


# Load Boston dataset
X, y = datasets.load_boston(return_X_y=True)
# Split train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate model Linear Regression and Ridge Regression
model1 = Rg.LinearRegression()
model2 = Rg.RidgeRegression()

alphas = [0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1, 2.5, 5, 7.5, 10]
score_model1 = []
score_model2 = []

for alpha in alphas:
    # Fit model on training data
    model1.fit(X_train, y_train)
    model2.set_params(alpha=alpha)
    model2.fit(X_train, y_train)
    # Calculate score on test data
    score_model1.append(model1.score(X_test, y_test))
    score_model2.append(model2.score(X_test, y_test))

# Plot alpha vs score
plt.figure(figsize=(8, 8))
plt.plot(alphas, score_model1, label='Linear Regression')
plt.plot(alphas, score_model2, label='Ridge Regression')
plt.legend()
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('R2 score')
plt.title('Model Performance')
plt.show()
