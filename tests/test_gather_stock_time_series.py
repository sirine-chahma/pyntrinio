# Author: Team Andrey Markov
# tests for gather_stock_time_series

from pyntrinio.pyntrinio import gather_stock_time_series
import pandas as pd
from datetime import datetime, date

# helper data
api_key = 'OjhlMjhjNTBmY2IyMWJiMWE0MTExYjQwNWZmZTVkZWM1'
ticker = 'AAPL'

# test that return type is dictionary by default
def test_default_output_type():
    """
    Test that return type is dictionary by default
    """
    assert type(gather_stock_time_series(api_key, ticker, start_date="2020-01-15", end_date="2020-01-25")) == dict

# test that return type is a pandas dataframe when specified
def test_pddf_output_type():
    """
    Test that return type is a pandas dataframe when specified
    """
    assert type(gather_stock_time_series(api_key, ticker, start_date="2020-01-15", end_date="2020-01-25", output_format='pddf')) == pd.core.frame.DataFrame

# test that you get an error when you put in an incorrect API key
def api_key_test():
    """
    Give a wrong api_key, see if the function correctly handles the exception.
    """
    msg = "Invalid API Key: please input a valid API key as a string"
    assert gather_stock_time_series('wrong api key!!', ticker, start_date="2020-01-15", end_date="2020-01-25") == msg
    
# test that you get an error when you put in an incorrect ticker format
def ticker_format_test():
    """
    Give a wrong ticker format, see if the function correctly handles the exception.
    """
    msg = "Invalid Input: ticker has to be a string, e.g. 'APPL'"
    assert gather_stock_time_series(api_key, 123, start_date="2020-01-15", end_date="2020-01-25") == msg
    assert gather_stock_time_series(api_key, ["AAPL", "CSCO"], start_date="2020-01-15", end_date="2020-01-25") == msg

# test that you get an error when you put in an invalid date format
def date_format_test():
    """
    See if the function correctly handles the input dates in wrong formats.
    """
    msg = "Invalid Date format - please input the date as a string with format %Y-%m-%d"
    assert gather_stock_time_series(api_key, ticker, start_date='2018-15-12') == msg

# test that you get an error when the end date is before the start date
def test_start_date_prior_to_end_date():
    """
    Test that you get an error when the end date is before the start date
    """
    msg = "Invalid Input: end_date must be later than start_date"
    assert gather_stock_time_series(api_key, ticker, start_date="2020-01-25", end_date="2020-01-15") == msg

# test that you get a valid output shape when you put in no start date
def test_end_date_only_shape():
    """
    Test that you get a valid output shape when you put in no start date
    """
    assert gather_stock_time_series(api_key, ticker, end_date="2020-01-25", output_format='pddf').shape[0] > 0

# test that you get a valid output shape when you put in no end date
def test_start_date_only_shape():
    """
    Test that you get a valid output shape when you put in no end date
    """
    assert gather_stock_time_series(api_key, ticker, start_date="2020-01-15", output_format='pddf').shape[0] > 0

# test that you get a valid output shape when you don't put in a start or end date
def test_no_dates_shape():
    """
    Test that you get a valid output shape when you don't put in a start or end date
    """
    assert gather_stock_time_series(api_key, ticker, output_format='pddf').shape[0] > 0

# test the output values for a start and end date
def test_output():
    """
    Test the output values for a start and end date
    """
    results = {'date': [date(2020, 1, 17), date(2020, 1, 16), date(2020, 1, 15)],
    'close': [318.73, 315.24, 311.34],
    'adj_close': [317.975342701639, 314.493605977676, 310.60284001107],
    'high': [318.74, 315.7, 315.5],
    'adj_high': [317.98531902463, 314.952516835276, 314.75299037545],
    'low': [315.0, 312.09, 309.55],
    'adj_low': [314.254174225885, 311.351064235417, 308.817078195627],
    'open': [316.27, 313.59, 311.85],
    'adj_open': [315.52116724578, 312.847512684112, 311.111632483626],
    'volume': [34454117.0, 27207254.0, 30480882.0],
    'adj_volume': [34454117.0, 27207254.0, 30480882.0],
    'frequency': ['daily', 'daily', 'daily'],
    'intraperiod': [False, False, False]}
    assert gather_stock_time_series(api_key, ticker, start_date='2020-01-15', end_date='2020-01-17') == results
