import data, portfolio, charts, ml
import numpy as np
import pprint
import time

symbols = ['SPY']
pprint.pprint(symbols)

alloc = np.ones(len(symbols)) / len(symbols)
df = data.get(symbols, '2016-11-08', '2017-01-30')

# Regular distribution run
portA = portfolio.stats(df, alloc, 100000)
x = df.index.values.astype(int) / 1000000000
y = df['SPY'].values

# Test Linear Regression Learner
learner1 = ml.LinRegLearner()
learner1.train(x,y)
epoch = int(time.mktime(time.strptime('2017-02-06', '%Y-%m-%d')))
print learner1.query(epoch)


# Test KNN Learner
learner2 = ml.KNNLearner()
learner2.train(x,y)
print learner2.query(epoch)
