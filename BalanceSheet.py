import pandas as pd
import requests

#%%
def bsimport(stock):
    pd.set_option('display.max_columns', 5)
    df = requests.get(f'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/%s?period=quarter&apikey=1e2138433b211719b20c08b687be3bd9' % stock)
    df = df.json()
    df = df['financials']
    df = pd.DataFrame.from_dict(df) #Tranform from dictionary to Dataframe
    df = df.set_index('date',drop=True)
    df = df.astype(float)
    df = df.div(1000000)
    df = df.astype(int)
    df = df.T
    return df


