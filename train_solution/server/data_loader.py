import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from penguin_sample import PenguinSample

class DataLoader():
    def __init__(self, test_size = 0.2, scale = True):
        self.test_size = test_size
        self.scale = scale
        self.scaler = StandardScaler()
        self._island_map = {}
        self._sex_map = {}

    def load_preprocess(self, path):
        data = pd.read_csv(path)

        data = self._feature_engineering_pipeline(data)

        X = data.drop(['species', "island", "sex"], axis=1)

        if(self.scale):
            X = self.scaler.fit_transform(X) 

        y = data['species']
        spicies = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
        y = [spicies[item] for item in y]
        y = np.array(y) 

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=33)

        return X_train, X_test, y_train, y_test

    def prepare_sample(self, raw_sample: PenguinSample):
        island = self._island_map[raw_sample.island]
        sex = self._sex_map[raw_sample.sex]

        sample = [raw_sample.culmenLength, raw_sample.culmenDepth, raw_sample.flipperLength, raw_sample.bodyMass, island, sex]
        sample = np.array([np.asarray(sample)]).reshape(-1, 1)

        if(self.scale):
            self.scaler.fit_transform(sample)

        return sample.reshape(1, -1)

    def _feature_engineering_pipeline(self, data):
        data['culmen_length_mm'].fillna((data['culmen_length_mm'].mean()), inplace=True)
        data['culmen_depth_mm'].fillna((data['culmen_depth_mm'].mean()), inplace=True)
        data['flipper_length_mm'].fillna((data['flipper_length_mm'].mean()), inplace=True)
        data['body_mass_g'].fillna((data['body_mass_g'].mean()), inplace=True)

        data["species"] = data["species"].astype('category')
        data["island"] = data["island"].astype('category')
        data["sex"] = data["sex"].astype('category')

        data["island_cat"] = data["island"].cat.codes
        data["sex_cat"] = data["sex"].cat.codes

        self._island_map = dict(zip(data['island'], data['island'].cat.codes))
        self._sex_map = dict(zip(data['sex'], data['sex'].cat.codes))

        return data