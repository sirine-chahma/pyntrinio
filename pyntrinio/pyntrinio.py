# Author: Team Andrey Markov
# pyntrinio functions

# Imports
import pandas as pd
import intrinio_sdk
from datetime import datetime

# Function that gathers a given financial statement for a given company for a specified time
def gather_financial_statement_time_series(api_key, ticker, statement, year, period, output_format='dict'): 
  """
  Given the tickers, statement, year and period returns all the financial information from the Intrinio API stock data
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  ticker : str
    the ticker symbol you would like to get information for
  statement : str
    the statement that you want to study
  year : list
    the list containing the years as strings
  period : list
    the list of quarters for which you want information
  output_format : str (optional, default = 'dict')
    the output format for the data, options are 'dict' for dictionary or 'pddf' for pandas dataframe  

  Returns
  -----------
  pandas.core.frame.DataFrame
    a dataframe that contains the financial information for a given company for the mentioned period

  Example
  -----------
  >>> gather_financial_statement_time_series(api_key, 'AAPL', 'income_statement', ['2018,'2019'], ['Q1'])
  {'AAPL' : [
  {'ticker': ['AAPL'],
  'year': ['2018'],
  'period': ['Q1'],
  'RevenueFromContractWithCustomerExcludingAssessedTax': [16145000000.0],
  'CostOfGoodsAndServicesSold': [104262000000.0],
  'GrossProfit': [21078007000.0],
  'ResearchAndDevelopmentExpense': [396090000.0],
  'SellingGeneralAndAdministrativeExpense': [482045600.0],
  'OperatingExpenses': [7899000000.0],
  'OperatingIncomeLoss': [2388230000.0],
  'NonoperatingIncomeExpense': [470000000.0],
  'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': [13906050000.0],
  'IncomeTaxExpenseBenefit': [3986500000.0],
  'NetIncomeLoss': [20970000000.0],
  'EarningsPerShareBasic': [4.17],
  'EarningsPerShareDiluted': [4.13],
  'WeightedAverageNumberOfSharesOutstandingBasic': [4658920000.0],
  'WeightedAverageNumberOfDilutedSharesOutstanding': [4874252000.0]},
  {'ticker': ['AAPL'],
  'year': ['2019'],
  'period': ['Q1'],
  'RevenueFromContractWithCustomerExcludingAssessedTax': [168620000000.0],
  'CostOfGoodsAndServicesSold': [104558000000.0],
  'GrossProfit': [32031000000.0],
  'ResearchAndDevelopmentExpense': [3902000000.0],
  'SellingGeneralAndAdministrativeExpense': [4783000000.0],
  'OperatingExpenses': [8685000000.0],
  'OperatingIncomeLoss': [23346000000.0],
  'NonoperatingIncomeExpense': [560000000.0],
  'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': [23906000000.0],
  'IncomeTaxExpenseBenefit': [3941000000.0],
  'NetIncomeLoss': [19965000000.0],
  'EarningsPerShareBasic': [4.22],
  'EarningsPerShareDiluted': [4.18],
  'WeightedAverageNumberOfSharesOutstandingBasic': [4735820000.0],
  'WeightedAverageNumberOfDilutedSharesOutstanding': [4773252000.0]}
  ]}  
  """
  
  if output_format=='dict':
    results={}
  else:
    results=pd.DataFrame(results)
  
  return results

# Function that gathers a given statement at a specific time for different companies
def gather_financial_statement_company_compare(api_key, ticker, statement, year, period, output_format='dict'): 
  """
  Given the tickers, statement, year and period returns all the information from the Intrinio API fundamental reported financials
    for that time and those tickers in either a dictionary or a pandas dataframe format.
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  ticker : list
    a list of the ticker symbols you would like to study
  statement : str
    the statement that you want to study
  year : str
    the year you want the information from
  period : str
    the period you want the information from
  output_format : str (optional, default = 'dict')
    the output format for the data, options are 'dict' for dictionary or 'pddf' for pandas dataframe
    
  Returns
  -----------
  object of type output_format
    information about the given statement for the given tickers at the given time in the specified output format
  
  Example
  -----------
  >>> gather_financial_statement_company_compare(api_key, ['AAPL', 'CSCO'], 'income_statement', '2019', 'Q1')
  {'AAPL' : {'ticker': ['AAPL'],
  'year': ['2019'],
  'period': ['Q1'],
  'RevenueFromContractWithCustomerExcludingAssessedTax': [168620000000.0],
  'CostOfGoodsAndServicesSold': [104558000000.0],
  'GrossProfit': [32031000000.0],
  'ResearchAndDevelopmentExpense': [3902000000.0],
  'SellingGeneralAndAdministrativeExpense': [4783000000.0],
  'OperatingExpenses': [8685000000.0],
  'OperatingIncomeLoss': [23346000000.0],
  'NonoperatingIncomeExpense': [560000000.0],
  'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': [23906000000.0],
  'IncomeTaxExpenseBenefit': [3941000000.0],
  'NetIncomeLoss': [19965000000.0],
  'EarningsPerShareBasic': [4.22],
  'EarningsPerShareDiluted': [4.18],
  'WeightedAverageNumberOfSharesOutstandingBasic': [4735820000.0],
  'WeightedAverageNumberOfDilutedSharesOutstanding': [4773252000.0]},
 'CSCO' : {'ticker': ['CSCO'],
  'year': ['2019'],
  'period': ['Q1'],
  'RevenueFromContractWithCustomerExcludingAssessedTax': [26145000000.0],
  'CostOfGoodsAndServicesSold': [9852000000.0],
  'GrossProfit': [8146000000.0],
  'ResearchAndDevelopmentExpense': [1608000000.0],
  'SellingAndMarketingExpense': [2410000000.0],
  'GeneralAndAdministrativeExpense': [211000000.0],
  'AmortizationOfIntangibleAssets': [34000000.0],
  'RestructuringAndOtherCharges': [78000000.0],
  'OperatingExpenses': [4341000000.0],
  'OperatingIncomeLoss': [3805000000.0],
  'InvestmentIncomeInterestAndDividend': [344000000.0],
  'InterestExpense': [221000000.0],
  'OtherNonoperatingIncomeExpense': [-19000000.0],
  'NonoperatingIncomeExpense': [104000000.0],
  'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': [3909000000.0],
  'IncomeTaxExpenseBenefit': [360000000.0],
  'NetIncomeLoss': [3549000000.0],
  'EarningsPerShareBasic': [0.78],
  'EarningsPerShareDiluted': [0.77],
  'WeightedAverageNumberOfSharesOutstandingBasic': [4565000000.0],
  'WeightedAverageNumberOfDilutedSharesOutstanding': [4614000000.0]}}
  """
  
  if output_format=='dict':
    results={}
  else:
    results=pd.DataFrame(results)
  
  return results


# Function that gathers time series data of stock values
def gather_stock_time_series(api_key, ticker, start_date=None, end_date=None, output_format='dict'):
  """
  Given the ticker, start date, and end date, return from the Intrinio API stock data
    for that time frame in either a dictionary or a pandas dataframe format.
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  ticker : str
    the ticker symbol you would like to get stock data for
  start_date : str (optional)
    the earliest date in the format of "%Y-%m-%d", e.g. "2019-12-31" to get data for
  end_date : str (optional)
    the most recent date in the format of "%Y-%m-%d", e.g. "2019-12-31" to get data for
  output_format : str (optional, default = 'dict')
    the output format for the data, options are 'dict' for dictionary or 'pddf' for pandas dataframe
    
  Returns
  -----------
  object of type output_format
    stock data for the specific timeframe in the specified output format
  
  Example
  -----------
  >>> gather_stock_time_series(api_key, 'AAPL')
  """
  try:
    # change dates to datetime objects
    if start_date is not None:
      start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if end_date is not None:
      end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
  except:
    print("Invalid Date format - please input the date as a string with format %Y-%m-%d")
    return
  
  try:
    # initialize API key
    intrinio_sdk.ApiClient().configuration.api_key['api_key'] = api_key
    
    # initialize security API
    security_api = intrinio_sdk.SecurityApi()
    
    # put stock prices into a variable
    stock_prices = security_api.get_security_stock_prices(ticker, start_date=start_date, end_date=end_date, page_size=10000).stock_prices
  except:
    print("Incorrect API Key - please input a valid API key as a string")
    return
    
  # initialize a results dictionary
  results = {'date':[], 'close':[], 'adj_close':[], 'high':[], 'adj_high':[], 'low':[], 'adj_low':[], 
            'open':[], 'adj_open':[], 'volume':[], 'adj_volume':[], 'frequency':[], 'intraperiod':[]}

  # fill in dictionary
  for i in list(range(0, len(stock_prices), 1)):
      results['date'].append(stock_prices[i].date)
      results['close'].append(stock_prices[i].close)
      results['adj_close'].append(stock_prices[i].adj_close)
      results['high'].append(stock_prices[i].high)
      results['adj_high'].append(stock_prices[i].adj_high)
      results['low'].append(stock_prices[i].low)
      results['adj_low'].append(stock_prices[i].adj_low)
      results['open'].append(stock_prices[i].open)
      results['adj_open'].append(stock_prices[i].adj_open)
      results['volume'].append(stock_prices[i].volume)
      results['adj_volume'].append(stock_prices[i].adj_volume)
      results['frequency'].append(stock_prices[i].frequency)
      results['intraperiod'].append(stock_prices[i].intraperiod)
    
  # if the ouput format is a dataframe, change to that
  if output_format == 'pddf':
      results = pd.DataFrame(results)
    
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
    a dataframe that contains the companies, historical prices and corresponding profit/loss
  
  Example
  -----------
  >>> gather_stock_returns(api_key, ['AAPL', 'AMZON'], "2017-12-31", "2019-03-01")

  """
  
  results = pd.DataFrame()
  
  return results
