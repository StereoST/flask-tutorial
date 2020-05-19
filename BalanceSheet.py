import pandas as pd
import requests

#%%
def bsimport(stock):
    pd.set_option('display.max_columns', 5)
    df = requests.get(f'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/%s?period=quarter' % stock)
    df = df.json()
    df = df['financials']
    df = pd.DataFrame.from_dict(df) #Tranform from dictionary to Dataframe
    df = df.set_index('date',drop=True)
    # df = df.div(1000000)
    # df = df.T
    # print(df)
    return df

bsimport('AAPL')


