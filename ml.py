from scipy import stats
from sklearn import neighbors
import numpy as np
'''
# Linear Regression
learner = LinRegLearner() # Makes an instance of the learner
learner.train(Xtrain, Ytrain) # Trains the model with our data
Y = learner.query(Xtest) # run test data to get the y data

# KNN
learner = KNNLearner(k=3) # sets how many nearest neighbors to use
learner.train(Xtrain, Ytrain) # Trains the model with our data
Y = learner.query(Xtest) # run test data to get the y data

use numpy.corrcoef to measure correlation
'''

class LinRegLearner:
    def __init__(self):
        pass

    def train(self, X, Y):
        self.m, self.b, self.r_value, self.p_value, self.std_err = stats.linregress(X,Y)

    def query(self, X):
        y = self.m * X + self.b
        return y

class KNNLearner:
    def __init__(self, k=3):
        self.learner = neighbors.KNeighborsClassifier(n_neighbors=k)

    def train(self, X, Y):
        # Reshape X for KNN algo
        if (X.ndim == 1):
            X = np.reshape(X, (X.shape[0], 1))
        # Convert Y to integers (ie; *100)
        Y = Y * 100
        Y = Y.astype(int)
        self.learner.fit(X, Y)

    def query(self, X):
        return float(self.learner.predict(X)[0]) / 100
