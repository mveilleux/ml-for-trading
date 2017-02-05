import matplotlib.pyplot as plt
import pandas as pd

def plot(df, title=""):
    ''' Plot DataFrame '''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
