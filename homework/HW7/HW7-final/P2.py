import sqlite3

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


# Function to save the data to database
def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    cursor = db.cursor()

    # model_params
    model_params = model.get_params()
    for param_name in model_params.keys():
        vals_to_insert = (model_id, model_desc, param_name, model_params[param_name])
        cursor.execute('''INSERT INTO model_params (id, desc, param_name, value)
                          VALUES (?, ?, ?, ?)''', vals_to_insert)

    # model_coefs
    intercept = model.intercept_[0]
    coef = model.coef_[0]
    feature_names = data.feature_names
    cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value)
                      VALUES (?, ?, ?, ?)''', (model_id, model_desc, 'intercept', intercept))
    for i in range(coef.shape[0]):
        vals_to_insert = (model_id, model_desc, feature_names[i], coef[i])
        cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value)
                          VALUES (?, ?, ?, ?)''', vals_to_insert)

    # model_results
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    cursor.execute('''INSERT INTO model_results (id, desc, train_score, test_score)
                      VALUES (?, ?, ?, ?)''', (model_id, model_desc, train_score, test_score))


# Connect to database and drop table if exists
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS model_params')
cursor.execute('DROP TABLE IF EXISTS model_coefs')
cursor.execute('DROP TABLE IF EXISTS model_results')
cursor.execute('PRAGMA foreign_keys=1')

# Create tables
cursor.execute('''CREATE TABLE model_params (
               id INTEGER,
               desc TEXT,
               param_name TEXT,
               value FLOAT )''')
cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER,
               desc TEXT,
               feature_name TEXT,
               value FLOAT )''')
cursor.execute('''CREATE TABLE model_results (
               id INTEGER,
               desc TEXT,
               train_score FLOAT,
               test_score FLOAT )''')
db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

# Save to database
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

# Reduced logistic regression model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']
X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]
reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

# Save to database
save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# Logistic regression model with L1 penalty
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

# Save to database
save_to_database(3, 'L1 penalty model', db, penalized_model, X_train, X_test, y_train, y_test)

# Part C: Database queries
# Print the id of the best model and the corresponding test score
query = '''SELECT *, MAX(test_score) FROM model_results'''
best_model = cursor.execute(query).fetchall()
best_model_id = best_model[0][0]
best_model_test_score = best_model[0][3]
print(f'Best model id: {best_model_id}')
print(f'Best validation score: {best_model_test_score:.4f}')

# Print the feature names and the corresponding coefficients of that model
query = '''SELECT feature_name, value FROM model_coefs WHERE id = 3'''
coefs = cursor.execute(query).fetchall()
for coef in coefs:
    print(f'{coef[0]}: {coef[1]:.4f}')

# Reproduce the best score
test_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
test_model.fit(X_train, y_train)
# Manually change fit parameters
coef_list = [x[1] for x in coefs]   # Convert intercept and coefficients to a list
intercept = coef_list[0]            # Get intercept
coef = coef_list[1:]                # Get coefficients
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])
test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score:.4f}')

db.commit()
db.close()
