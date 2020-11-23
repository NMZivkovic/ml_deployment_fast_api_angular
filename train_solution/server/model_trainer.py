from data_loader import DataLoader
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from penguin_sample import PenguinSample

class ModelTrainer():
    def __init__(self, algoritm, test_size=0.2):
        if(algoritm == 'svm'):
            self.data_loader = DataLoader()
            self.model = SVC(kernel="rbf", gamma=0.1, C=500, verbose=True)

        if(algoritm == 'logistic regression'):
            self.data_loader = DataLoader()
            self.model = LogisticRegression(C=1e20, verbose=True)
        
        if(algoritm == 'decision tree'):
            self.data_loader = DataLoader(scale = False)
            self.model = DecisionTreeClassifier(max_depth=5)

        if(algoritm == 'random forest'):
            self.data_loader = DataLoader(scale = False)
            self.model = RandomForestClassifier(n_estimators=11, max_leaf_nodes=16, n_jobs=-1, verbose=True)

    def train(self, path):
        X_train, X_test, y_train, y_test = self.data_loader.load_preprocess(path)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        return accuracy_score(predictions, y_test)

    def predict(self, data: PenguinSample):
        prepared_sample = self.data_loader.prepare_sample(data)
        return self.model.predict(prepared_sample)
