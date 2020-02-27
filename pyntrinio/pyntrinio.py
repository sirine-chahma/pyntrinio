# Author: Team Andrey Markov
# pyntrinio functions

# Imports
import pandas as pd
import intrinio_sdk
import datetime

# Function that gathers time series data of stock values
def gather_stock_time_series(api_key, ticker, start_date, end_date, output_format='dict'):
  """
  Given the ticker, start date, and end date, return from the Intrinio API stock data
    for that time frame in either a dictionary or a pandas dataframe format.
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  ticker : str
    the ticker symbol you would like to get stock data for
  start_date : datetime.date (optional)
    the earliest date you would like to get stock data for
  end_date : datetime.date (optional)
    the most recent date you would like to get stock data for
  output_format : str (optional, default = 'dict')
    the output format for the data, options are 'dict' for dictionary or 'pddf' for pandas dataframe
    
  Returns
  -----------
  object of type output_format
    stock data for the specific timeframe in the specified output format
  
  Example
  -----------
  >>> gather_stock_time_series(api_key, 'AAPL')
  {'ticker':['AAPL'], 'adj_close':[300], 'date':[datetime.date(2020, 1, 2)]}
  """
  
  if output_format=='dict':
    results={}
  else:
    results=pd.DataFrame(results)
  
  return results


# Function that calculates the stock returns
def gather_stock_returns(api_key, ticker, buy_date, sell_date):
  """
  Given the tickers, buy-in date, sell-out date, returns the historical prices and profit/loss.
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  tickers : list
    the list containing ticker symbols
  buy_date : str
    the buy-in date in the format of "%Y-%m-%d", e.g. "2019-12-31"
  end_date : str
    the sell-out date in the format of "%Y-%m-%d", e.g. "2019-12-31"
    
  Returns
  -----------
  pandas.core.frame.DataFrame
    stock data for the specific timeframe in the specified output format
  
  Example
  -----------
  >>> gather_stock_returns(api_key, ['AAPL', 'AMZON'], "2017-12-31", "2019-03-01")
 
  """
  
  results = pd.DataFrame()
  
  return results
