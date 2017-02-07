import pandas as pd
import pandas_datareader as pdr
import json, time, datetime, requests
import hashlib, hmac
import pprint
'''
Get Stock Data
'''
def get(symbols, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        tmp_df = pdr.DataReader(name=symbol, data_source='yahoo',
                        start=start_date, end=end_date)
        # This will be for later to save the results locally
        #df.to_csv(filename, index_label="Date")
        tmp_df = tmp_df[['Adj Close']].rename(columns={'Adj Close': symbol})
        df = df.join(tmp_df, how='inner')

    # Clean the data up
    df.fillna(method="ffill",inplace="TRUE")
    df.fillna(method="bfill",inplace="TRUE")

    return df

'''
Get Crypto Data
'''
def get_crypto(symbols, start_date, end_date):

    def dateparse (time):
        # Round to the nearest minute and return datetime
        return datetime.datetime.fromtimestamp( int(time) - int(time)%60 )

    for symbol in symbols:
        path = '/Users/mveilleux/Box Sync/Projects/ml/crypto-db/' + symbol + '.csv'
        df = pd.read_csv(path, header=None, index_col=0, parse_dates=True, date_parser=dateparse, names=['Ask', 'Bid', 'Last'])
        df = df[['Last']].rename(columns={'Last': symbol})

        if 'df_final' not in locals():
            df_final = df
        else:
            df_final = df_final.join(df, how='inner')

    return df_final

def crypto_to_usdt(df):

    if 'USDT-BTC' in df:
        # Drop USDT in temp dataframe
        tmp_df = df.drop(['USDT-BTC'], axis=1)
        tmp_df = tmp_df.multiply(df['USDT-BTC'], axis=0)
        tmp_df = tmp_df.rename(columns={col: col.replace('BTC','USDT') for col in df.columns})
        df = tmp_df.join(df['USDT-BTC'], how='inner')

    return df
