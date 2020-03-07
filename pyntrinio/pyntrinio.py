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
# Function that gathers a given financial statement for a given company for a specified time
def gather_financial_statement_time_series(api_key, ticker, statement, year, period, output_format = 'pddf'):
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
  output_format : str (optional, default = 'pddf')
    the output format for the data, options are 'dict' for dictionary or 'pddf' for pandas dataframe

  Returns
  -----------
  dictionary or pandas.core.frame.DataFrame
    a dictionary/dataframe that contains the financial information for a given company for the mentioned year(s) & period(s)

  Example
  -----------
  >>> gather_financial_statement_time_series(api_key, 'CVX', 'cash_flow_statement', ['2016','2017'], ['Q1','Q2','Q3'])
  >>> gather_financial_statement_time_series(api_key, 'CVX', 'cash_flow_statement', ['2016','2017'], ['Q1','Q2','Q3'], output_format = 'dict')
  
  """  
  ## Limited free access on intrino provides only Sandbox access
    
    # List of available tickers with sandbox key: 
    # https://product.intrinio.com/developer-sandbox/coverage/us-fundamentals-financials-metrics-ratios-stock-prices

  available_tickers = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'DWDP', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX', 'V', 'VZ', 'WMT', 'XOM']
    
  # https://data.intrinio.com/data-tags
  available_statements = ['income_statement', 'cash_flow_statement', 'balance_sheet_statement']

  inputs = {'api_key':api_key, 'ticker': ticker, 'statement':statement}
    
  ## Check if api_key, ticker and statement are strings
    
  for inst in inputs.keys():
    if not isinstance(inputs[inst], str):
      raise Exception("Sorry, " + inst + " must be a string")    
    
  ## Check if the output_format is either 'dict' or 'pddf' 
  if not output_format in ['dict', 'pddf']:
    raise Exception("Sorry, output_format must be 'dict' or 'pddf'.")
        
  if not statement in available_statements:
      raise Exception("Valid entries for statement can either be 'income_statement' or 'cash_flow_statement' or 'balance_sheet_statement'.")    
    
  if not ticker in available_tickers:
    raise Exception("Valid entries for ticker provided in the Readme.md")    

  ## Check the type of year and period as list  
  if not type(year) is list:
      raise TypeError("year has to be a list of strings. For ex. ['2016','2017'].")
    
  if not type(period) is list:
      raise TypeError("period has to be a list of strings/ For ex. ['Q1'].")     

  for y in year:
    if not len(y)== 4:
      raise Exception("Sorry, year must be a string of 4 digits")

  ## Tests Over ##  

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

  final_df = pd.DataFrame(results)

  ## if_else for output format
    
  if output_format == 'pddf':
      return final_df
  else:
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
  """    

  statements = ['income_statement', 'balance_sheet_statement', 'cash_flow_statement']

  inputs = {'api_key':api_key, 'statement':statement, 'year':year, 'period':period}
  #Check if api_key, statement, year, period are strings
  for inst in inputs.keys():
    if not isinstance(inputs[inst], str):
      raise TypeError("Sorry, " + inst + " must be a string")
          
  #Check if ticker is a list
  if not isinstance(ticker, list):
    raise TypeError("Sorry, ticker must be a list")
  
  #Check if the year is a 4-digits number
  if not len(year)==4:
    raise Exception("Sorry, year must be a string with 4 digits")
  

  #Check if the output_format is either 'dict' or 'pddf' 
  if not output_format in ['dict', 'pddf']:
    raise Exception("Sorry, output_format must be 'dict' or 'pddf'.")

  #Check if the statement is valid
  if not statement in statements:
    raise Exception('Sorry, the statement is not correct')
  
  
  #link with the API
  intrinio_sdk.ApiClient().configuration.api_key['api_key'] = api_key
  fundamentals_api = intrinio_sdk.FundamentalsApi()
  
  #result will contain a dictionnary for each company.
  #This dictionnary will contain all the information for one company
  result = []

  #for every company
  for comp in ticker : 
    #key is the appropriate key to select the information we want
    key = comp + '-' + str(statement) + '-' + str(year) + '-' + str(period)
    #get the object that we want from the API
    fundamentals = fundamentals_api.get_fundamental_reported_financials(key)
    my_fund = fundamentals.reported_financials

    #This dictionnary will contain all the information for one company
    dict ={}
    dict['ticker'] = comp
    dict['statement'] = statement
    dict['year'] = year
    dict['period'] = period
      
    #we store all the values, balances, names and the tags
    for i in range(len(my_fund)):
      value = my_fund[i].value
      tag_dic = my_fund[i].xbrl_tag
      balance = tag_dic.balance
      name = tag_dic.name
      tag = tag_dic.tag
      #tag is a key of this dictionnary
          
      #if the tag is several times in the original object, we keep one tag and the 
      # value is the sum or the substraction of all the values of this tag 
      # (depending on the value of balance) 
      if tag in dict.keys():
        if balance == 'credit':
          value = dict[tag]['value'] - value
        else : 
           value = dict[tag]['value'] + value
      dict[tag] = {'value' : value, 'balance': balance, 'name': name}
    result.append(dict)
      
  if output_format == 'dict':
    return result
  
  #if the wanted type of the output is a dataframe
  else:
    #initialize a new empty dictionnary that we will convert into a dataframe
    #this dictionnary will have the following structure
    # {'name': [name1, name2], 'revenue' : [revenu_company_1, revenue_company_2], ...}
    df = {}
    
    #for every company
    for i in range(len(result)):
          
      #select all the information about this company
      sub_dict = result[i]
            
      #For all the tags that we have for this company
      for val in sub_dict.keys():
                
        #if the key is already in the df dictionnary
        if val in df.keys():
                  
          #if the value that corresponds to the key is a string 
          # which means that the key is 'ticker', 'statement', 'year' or 'period'
          if type(sub_dict[val]) == str:
                        
            #We appen the value of the key
            df[val].append(sub_dict[val])
                        
          #if the value of the key is a dictionnary
          else:
                        
            #only take the value that corresponds to the key 'value'
            df[val].append(sub_dict[val]['value'])
                
        #This step is to make sure that all the values in this dictionnary
        # (which are lists) are the same length
        #if the tag of the company is not already in the df dictionnary
        else:

          if type(sub_dict[val]) == str:
            #We have to put as many 'None' as the number of companies for 
            # which we already collected the information 
            df[val] = [None for j in range(i)] + [sub_dict[val]]
          else:
            df[val] = [None for j in range(i)] + [sub_dict[val]['value']]
      # We add some 'None' to make sure that all the values are the same 
      #length in this dictionnary
      for val in df.keys():
        #The length of each value should be i+1 (=number of companies we studied)
        if len(df[val]) != i+1:
          df[val].append(None)
                  
  return pd.DataFrame(df)
                    


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