from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from penguin_sample import PenguinSample
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np

class ModelLoader():
    def __init__(self, algoritm):
        self.scaledData = True
        self._island_map = {'Torgersen': 2, 'Biscoe': 0, 'Dream': 1}
        self._sex_map = {'MALE': 2, 'FEMALE': 1}
        if(algoritm == 'svm'):
            self.model = load('./models/svm.joblib')

        if(algoritm == 'logistic regression'):
            self.model = load('./models/decision_tree.joblib')
        
        if(algoritm == 'decision tree'):
            self.scaledData = False
            self.model = load('./models/random_forest.joblib')

        if(algoritm == 'random forest'):
            self.scaledData = False
            self.model = load('./models/logistic_regression.joblib')

        self.scaler = StandardScaler()

    def prepare_sample(self, raw_sample: PenguinSample):
        island = self._island_map[raw_sample.island]
        sex = self._sex_map[raw_sample.sex]

        sample = [raw_sample.culmenLength, raw_sample.culmenDepth, raw_sample.flipperLength, raw_sample.bodyMass, island, sex]
        sample = np.array([np.asarray(sample)]).reshape(-1, 1)

        if(self.scaledData):
            self.scaler.fit_transform(sample)

        return sample.reshape(1, -1)

    def predict(self, data: PenguinSample):
        prepared_sample = self.prepare_sample(data)
        return self.model.predict(prepared_sample)
