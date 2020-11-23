import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from joblib import dump

def load_data(scale = True):
    data = pd.read_csv('./data/penguins_size.csv')

    data['culmen_length_mm'].fillna((data['culmen_length_mm'].mean()), inplace=True)
    data['culmen_depth_mm'].fillna((data['culmen_depth_mm'].mean()), inplace=True)
    data['flipper_length_mm'].fillna((data['flipper_length_mm'].mean()), inplace=True)
    data['body_mass_g'].fillna((data['body_mass_g'].mean()), inplace=True)

    data["species"] = data["species"].astype('category')
    data["island"] = data["island"].astype('category')
    data["sex"] = data["sex"].astype('category')

    data["island_cat"] = data["island"].cat.codes
    data["sex_cat"] = data["sex"].cat.codes

    X = data.drop(['species', "island", "sex"], axis=1)

    if(scale):
        scaler = StandardScaler()
        X = scaler.fit_transform(X) 

    y = data['species']
    spicies = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
    y = [spicies[item] for item in y]
    y = np.array(y) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)
    return X_train, X_test, y_train, y_test

# Train SVM
X_train, X_test, y_train, y_test = load_data(scale=True)
model = SVC(kernel="rbf", gamma=0.1, C=500, verbose=True)
model.fit(X_train, y_train)
dump(model, './models/svm.joblib') 

# Train Decision Tree
X_train, X_test, y_train, y_test = load_data(scale=False)
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
dump(model, './models/decision_tree.joblib') 

# Train Random Forest
X_train, X_test, y_train, y_test = load_data(scale=False)
model = RandomForestClassifier(n_estimators=11, max_leaf_nodes=16, n_jobs=-1, verbose=True)
model.fit(X_train, y_train)
dump(model, './models/random_forest.joblib') 

# Train Logistic Regression
X_train, X_test, y_train, y_test = load_data(scale=True)
model = LogisticRegression(C=1e20, verbose=True)
model.fit(X_train, y_train)
dump(model, './models/logistic_regression.joblib') 