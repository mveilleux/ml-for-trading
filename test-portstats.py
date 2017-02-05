import data, portfolio, charts
import numpy as np
import pprint

#symbols = ['FFFPX', 'FSRIX', 'ISTIX', 'JATTX', 'JMGRX', 'OIGYX'] # Curret fund
symbols = ['AAPL', 'GOOG', 'ORCL', 'MSFT', 'AMZN', 'CANN']
#symbols = ['FSSVX', 'JATTX', 'PSCSX', 'ESPNX']          # Small Caps
#symbols += ['FLVIX', 'FSCKX', 'JMGRX', 'VEVIX']          # Mid Caps
#symbols += ['FINSX', 'FUSVX', 'JDESX', 'OYEIX', 'PABGX'] # Large Caps
#symbols = ['ESPNX', 'VEVIX', 'FUSVX']
pprint.pprint(symbols)

alloc = np.ones(len(symbols)) / len(symbols)
df = data.get(symbols, '2016-01-01', '2017-01-30')

# Regular distribution run
portA = portfolio.stats(df, alloc, 100000)
pprint.pprint(portA['stats'])
charts.plot(portA['value'])

# Optimization
optimized = portfolio.opt_alloc(df)

#Optimized run
portB = portfolio.stats(df, optimized.x, 100000)
pprint.pprint(optimized)
pprint.pprint(portB['stats'])
charts.plot(portB['value'])
