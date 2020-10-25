from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as Rg


# Load Boston dataset
X, y = datasets.load_boston(return_X_y=True)
# Split train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate model Linear Regression and Ridge Regression
model1 = Rg.LinearRegression()
model2 = Rg.RidgeRegression()
# Set alpha for Ridge Regression
model2.set_params(alpha=0.1)

models = [model1, model2]
score_list = []

for model in models:
    # Fit on training data
    model.fit(X_train, y_train)
    # Score on test data
    score_list.append(model.score(X_test, y_test))

# Print R2 score for each model
print(f'R2 for Linear Regression is {score_list[0]:.4f}.')
print(f'R2 for Ridge Regression is {score_list[1]:.4f}.')

# Print parameters for the best model
if score_list[0] > score_list[1]:
    params = model1.get_params()
    print('Linear Regression is the best model.')
    print(f"Intercept: {params['intercept']:.4f}")
    print(f"Coefficients: {[round(x, 4) for x in params['coefficients']]}")
else:
    params = model2.get_params()
    print('Ridge Regression is the best model.')
    print(f"alpha: {params['alpha']:.4f}")
    print(f"Intercept: {params['intercept']:.4f}")
    print(f"Coefficients: {[round(x, 4) for x in params['coefficients']]}")