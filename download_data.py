from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import time
import os


def main():
    '''downloads historical stock data for s&p 500 companies from Alpha Vantage'''
    print('loading key...')
    with open('key.txt') as f:
        key = f.read()
    
    print('loading sp500 list...')
    table_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table_id = 'constituents'
    sp500 = pd.read_html(table_url, header = 0, attrs = {'id': table_id})[0]
    
    ts = TimeSeries(key=key, output_format='pandas')
    folder = 'data'
    num_requests = 0
    
    print('starting download loop...')
    start = time.time()
    
    for i, symbol in enumerate(sp500.Symbol):
        if num_requests % 5 == 0 and num_requests > 0:
            print(f'num_reqeusts: {i:<3d}  elapsed time: {(time.time()-start)/60:.2f} mins', end='')

            # wait for 1 minute and print dots every 10 seconds
            print('\t\t|', end='')
            for _ in range(60):
                print('.', end='')
                time.sleep(1)
            print('|')

        filename = os.path.join(folder, symbol + '.csv')

        if not os.path.exists(filename):
            try:
                get_full_data(ts, symbol).to_csv(filename)
            except KeyError as err:
                if 'Daily' in str(err):
                    print('Alpha Vantage daily API request limit reached (500)')
                    print('exiting for loop...')
                    break
            num_requests += 1
    
    print(f'DONE. {num_requests:d} requests completed')

            
def get_full_data(ts, symbol):
    data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')

    # remove numbers from beginning of column names
    data.columns = [c[3:] for c in data.columns]

    # drop unused columns
    data.drop(['dividend amount', 'split coefficient'], axis=1, inplace=True)

    # remove space from adjusted close column
    data.rename(columns={'adjusted close':'adj_close'}, inplace=True)

    # change data strings to datatimes
    data.index = pd.to_datetime(data.index)

    return data


if __name__ == '__main__':
    main()