# Author: Team Andrey Markov
# pyntrinio functions

# Imports
import pandas as pd
import intrinio_sdk
import datetime

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
  """    
  inputs = {'api_key':api_key, 'statement':statement, 'year':year, 'period':period}
  #Check if api_key, statement, year, period are strings
  for inst in inputs.keys():
    if not isinstance(inputs[inst], str):
      raise Exception("Sorry, " + inst + " must be a string")
          
  #Check if ticker is a list
  if not isinstance(ticker, list):
    raise Exception("Sorry, ticker must be a list")
  
  #Check if the ticker is valid
  
  #Check if the statement if valid
  
  #Check if the year is a 4-digits number
  if not len(year)==4:
    raise Exception("Sorry, year must be a string with 4 digits")
  

  #Check if the output_format is either 'dict' or 'pddf' 
  if not output_format in ['dict', 'pddf']:
    raise Exception("Sorry, output_format must be 'dict' or 'pddf'.")
  
  
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
