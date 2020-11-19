import pandas as pd
from pandas_datareader import data as web
from datetime import datetime, timedelta
import math


def costPrice_YF(df, time):
    """Function to calculate and add cost price in brazilian assets.
    The source is yahoo finance.
    The cost price is calculated by average close price sampled in
    certain period of time minus 1 standard deviation.
    df['codigo']: brazilian share real state assets such as HGRU11 or VISC11.
    Args:
        df([type]): pandas.core.frame.DataFrame
        time : period of time to consider cost price target.
        In case of NaN, cost price filled with 90% of current price.
    Returns:
        [type]: pandas.core.frame.DataFrame
        df['precocustoR$']: the column 'precocustoR$' is added in df
    """
    initial_date = datetime.now() - timedelta(time)
    df['codigo'] = df['codigo'].apply(lambda x: str(x).replace('11', '11.SA'))
    for i in df.index:
        share = df.at[i, 'codigo']
        dftmp = pd.DataFrame()
        dftmp = web.DataReader(share, data_source='yahoo', start=initial_date)
        dftmp = dftmp.drop(columns=['High', 'Low', 'Open', 'Volume',
                                    'Adj Close'])
        costprice = round((dftmp['Close'].mean()) - (dftmp['Close'].std()), 2)
        if math.isnan(costprice):
            costprice = round(0.9 * df.at[i, 'precoatualR$'], 2)
            print(f'{df.at[i, "codigo"]} : PrCusto = 90% PrAtual')
        df.at[i, 'precocustoR$'] = costprice
    df['codigo'] = df['codigo'].apply(lambda x: str(x).replace('11.SA', '11'))
    return df
