import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

pd.options.mode.chained_assignment = None

def get_full_df(symbol, folder='data'):
    '''load symbol csv as dataframe with date as index'''
    path = os.path.join(folder, symbol + '.csv')
    data = pd.read_csv(path, index_col=0)
    data.index = pd.to_datetime(data.index)
    data = add_changes(data)
    return data

def get_date_range(data, start, end):
    '''get data between and including start and end dates'''
    data = data[(data.index >= start) & (data.index <= end)]
    data.change.iloc[0] = np.nan # first day should not have a price change from previous day
    return data

def get_days(data, days=365):
    '''get past x days of data until today'''
    end = datetime.now()
    start = end - timedelta(days=days)
    return get_date_range(data, start, end)

def get_years(data, years=1):
    '''get past x years of data until today'''
    end = datetime.now()
    start = end - timedelta(days=years*365)
    return get_date_range(data, start, end)

def add_changes(data):
    '''add change from previous day to dataframe'''
    data['change'] = data.adj_close - data.adj_close.shift(1)
    return data