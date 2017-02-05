import numpy as np
import math
import scipy.optimize as spo

def stats(df, allocs, start_val=100000):
    normed = df / df.ix[0,:]
    #print normed.head(10)

    alloc = normed * allocs
    #print alloc.head(10)

    pos_vals = alloc * start_val
    #print pos_vals.head(10)

    port_val = pos_vals.sum(axis=1)
    #print port_val.head(10)

    # Daily Returns
    daily_rets = port_val.copy()
    daily_rets[1:] = (daily_rets[1:] / daily_rets[:-1].values) - 1
    daily_rets.ix[0] = 0
    #print "Daily Returns:"
    #print daily_rets

    # Cumulative Returns
    cum_ret = (port_val[-1] / port_val[0]) - 1
    #print "Cumulative Return: ", cum_ret

    # Average Daily Returns
    avg_daily_ret = daily_rets.mean()
    #print "Average Daily Return: ", avg_daily_ret

    # Standard Deviation of Daily Returns
    std_daily_ret = daily_rets.std()
    #print "Standard Deviation of Daily Return: ", std_daily_ret

    # Sharpe Ratio
    k = math.sqrt(252)
    sharpe_ratio = k * (avg_daily_ret / std_daily_ret)
    #print "Sharpe Ratio: ", sharpe_ratio

    return {
        'stats': {
            'cum_ret': cum_ret,
            'avg_daily_ret': avg_daily_ret,
            'std_daily_ret': std_daily_ret,
            'sharpe_ratio': sharpe_ratio
            },
        'normalized': normed,
        'positions': pos_vals,
        'value': port_val
        }

def error_alloc(C, data):
    """Compute error for portfolio as computed by the negative sharpe ratio.

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing portfolio allocations
    for the number of stocks in your portfolio.

    Returns error as negative sharpe ratio.
    """
    port = stats(data, C)
    err = port['stats']['sharpe_ratio'] * -1
    return err

def opt_alloc(data):
    def eq_constraint(C):
        return np.sum(C) - 1
    
    init_guess = np.ones(len(data.columns)) / len(data.columns)
    bounds = np.full( (len(data.columns), 2) , (0, 1), dtype='float_').tolist()
    result = spo.minimize(error_alloc, init_guess, args=(data,), method='SLSQP',
                          bounds=bounds, constraints={'type': 'eq', 'fun': eq_constraint},
                          options={'disp': True})

    return result
