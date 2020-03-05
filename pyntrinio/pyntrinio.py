# Author: Team Andrey Markov
# pyntrinio functions

# Imports
import pandas as pd
import numpy as np
import intrinio_sdk
from datetime import datetime, timedelta
from intrinio_sdk.rest import ApiException
from pytest import raises

# Function that gathers a given financial statement for a given company for a specified time
def gather_financial_statement_time_series(api_key, ticker, statement, year, period):
  """
  Given the tickers, statement, year and period returns the complete financial information from the Intrinio API stock data
  
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
    the list of quarters (as strings) for which you want information 

  Returns
  -----------
  pandas.core.frame.DataFrame
    a dataframe that contains the financial information for a given company for the mentioned year(s) & period(s)

  Example
  -----------
  >>> gather_financial_statement_time_series(api_key, 'CVX', 'cash_flow_statement', ['2016','2017'], ['Q1','Q2','Q3'])
  
  """  
  ## Limited free access on intrino provides only Sandbox access
    
    # List of available tickers with sandbox key: 
    # https://product.intrinio.com/developer-sandbox/coverage/us-fundamentals-financials-metrics-ratios-stock-prices

  available_tickers = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'DWDP', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX', 'V', 'VZ', 'WMT', 'XOM']
    
  # https://data.intrinio.com/data-tags
  available_statements = ['income_statement', 'cash_flow_statement', 'balance_sheet_statement']    
    
    ## Asserts    
  if not type(api_key) is str:
      raise TypeError("api_key has to be of type string")
    
  if not type(ticker) is str:
      raise TypeError("Ticker has to be of type string")
   
  if not type(statement) is str:
      raise TypeError("Statement has to be of type string")
        
  if not statement in available_statements:
      raise Exception("Valid entries for statement can either be 'income_statement' or 'cash_flow_statement' or 'balance_sheet_statement'.")    
    
  if not ticker in available_tickers:
    raise Exception("Valid entries for ticker provided in the Readme.md")    
    
  if not type(year) is list:
      raise TypeError("year has to be a list of strings. For ex. ['2016','2017'].")
    
  if not type(period) is list:
      raise TypeError("period has to be a list of strings/ For ex. ['Q1'].")     

  
  # Initialize API key
  intrinio_sdk.ApiClient().configuration.api_key['api_key'] = api_key
  fundamentals_api = intrinio_sdk.FundamentalsApi()
    
  # Empty list to store results: reformat later to dataframe
  results = []
  ## Outer loop over years, inner loop over quarters
  for i in year:
      for j in period:
        # define key to obtain relevant information
        key = str(ticker) + '-' + str(statement) + '-' + str(i) + '-' + str(j)
        # Obtain req. object from API
        fundamentals = fundamentals_api.get_fundamental_reported_financials(key)
        my_fund = fundamentals.reported_financials          
               
        # Empty dictionary to append the results : convert to df at the last stage
        my_dict ={}
        my_dict['ticker'] = ticker
        my_dict['statement'] = statement
        my_dict['year'] = i
        my_dict['period'] = j
    
        for n in range(0, len(my_fund)):
          my_dict[str(my_fund[n].xbrl_tag.tag)] = []
    
        # add values to the dictionary
        for k in range(0, len(my_fund)):
            for key, val in my_dict.items():
                if my_fund[k].xbrl_tag.tag == key:
                  my_dict[key].append(my_fund[k].value)
                  my_dict[key] = [sum(my_dict[key])]
        results.append(my_dict)            
  return pd.DataFrame(results)

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
  Given the tickers, buy-in date, sell-out date, returns the historical prices and profit/loss (based on the adjusted closing prices).
  
  Parameters
  -----------
  api_key : str
    API key (sandbox or production) from Intrinio
  tickers : list or str
    a single ticker or a list containing tickers. e.g. 'AAPL' or ['AAPL', 'CSCO']
  buy_date : str
    the buy-in date in the format of "%Y-%m-%d", e.g. "2019-12-31". If the input date is not a trading day, it will be automatically changed to the next nearest trading day. 
  sell_date : str
    the sell-out date in the format of "%Y-%m-%d", e.g. "2019-12-31". If the input date is not a trading day, it will be automatically changed to the last nearest trading day. 
    
  Returns
  -----------
  pandas.core.frame.DataFrame
    a dataframe that contains the companies, historical prices and corresponding profit/loss
  
  Example
  -----------
  >>> gather_stock_returns(api_key, ['AAPL', 'CSCO'], "2017-12-31", "2019-03-01")
  
  """
  
  # test whether the input dates are in the right format
  try:
    buy_date = datetime.strptime(buy_date, '%Y-%m-%d').date()
    sell_date = datetime.strptime(sell_date, '%Y-%m-%d').date()
    if buy_date >= sell_date:
      print("Invalid Input: `sell_date` is earlier than `buy_date`.")
      return
  except:
    print("Invalid Date format - please input the date as a string with format %Y-%m-%d")
    return
  
  if type(ticker) == str: # if user gives just one ticker
    ticker = [ticker]

  # initialize API key
  intrinio_sdk.ApiClient().configuration.api_key['api_key'] = api_key
  
  # initialize security API
  security_api = intrinio_sdk.SecurityApi()
  
  # test if the API Key works
  try:
    security_api.get_security_stock_prices(ticker[0], start_date=buy_date, end_date=sell_date)
  except:
    print("Incorrect API Key - please input a valid API key as a string")
    return

  # create the result DataFrame to record and report
  results = pd.DataFrame(columns = ['Stock', 'Buy date', 'Buy price', 'Sell date', 'Sell price', 'Return (%)'],
                     index = range(len(ticker)))

  # iterate through all the tickers and record the results
  i=0
  buy_date_upper = buy_date + timedelta(days=10) # if buy_date it not a trading day (holiday), we'll get the nearest next trading day instead
  sell_date_lower = sell_date - timedelta(days=10) # the same idea for sell_date, but we'll get the nearest **last** trading day instead.
  
  for ticker in ticker:
      api_response = security_api.get_security_stock_prices(ticker, start_date=buy_date, end_date=buy_date_upper)
      buy_price = api_response.stock_prices[-1].adj_close
      buy_date = api_response.stock_prices[-1].date.strftime("%Y-%m-%d")
      
      api_response = security_api.get_security_stock_prices(ticker, start_date=sell_date_lower, end_date=sell_date)
      sell_price = api_response.stock_prices[0].adj_close
      sell_date = api_response.stock_prices[0].date.strftime("%Y-%m-%d")
      rtn = ((sell_price - buy_price) / buy_price)*100
      rtn = round(rtn, 2)

      results.iloc[i,:] = [ticker, buy_date, buy_price, sell_date, sell_price, rtn]
      i+=1

  return results
