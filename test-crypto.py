import data, charts

df = data.get_crypto(['USDT-BTC', 'BTC-ETH', 'BTC-SYS', 'BTC-ZEC', 'BTC-XMR'], "x", "x")
df = data.crypto_to_usdt(df)

df_norm = df / df.ix[0,:]

print df.corr(method='pearson')

charts.plot(df_norm)
