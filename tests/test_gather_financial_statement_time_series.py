## Reference: https://ubc-mds.github.io/py-pkgs/testing.html#pytest-tests

from pyntrinio.pyntrinio import gather_financial_statement_time_series
from pytest import raises

# Sample data for testing
api_key = 'OjQ0YzljN2E4ODk5YzM1MzVhMTZmNTUwNmE2N2M0NTYz'
ticker = 'CVX'
statement = 'income_statement'
year = ['2017', '2018']
period = ['Q1','Q3']


def test_api_key_format():
    """
    Test if the api_key is a string
    """
    with raises(Exception):
        gather_financial_statement_time_series(OjQ0Yz, ticker, statement, year, period)

def test_ticker_format():
    """
    Test if the ticker is a string and available in a list of valid tickers
    """
    with raises(Exception):
        gather_financial_statement_time_series(api_key, CVX, statement, year, period)

    with raises(Exception):
        gather_financial_statement_time_series(api_key, 'CVSD', statement, year, period)

def test_output_format():
    """
    Test if the output format is of correct type ie a string ('dict' or 'pddf')
    """
    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, year, period, output_format = dict)

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, year, period, output_format = 'pdf')

def test_year_format():
    """
    Test if the year is a list of strings and the year(s) are of length 4
    """
    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, ['201', '2018'], period, output_format = 'pddf')

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, '2017', period)    

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, ['2017' '2018'], period) 

def test_statement_format():
    """
    Test if the statement is a string and available in a list of valid statement options
    """
    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, income_statement, year, period, output_format = 'pddf')

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, 'income_statemen', year, period)

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, ['income_statement'], year, period)    

def test_period_format():
    """
    Test if the period is a list of strings
    """
    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, 'income_statement', year, 'Q1')

    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, 'income_statement', year, Q1)
