# Author: Team Andrey Markov
# tests for gather_financial_statement_time_series

# Reference: https://ubc-mds.github.io/py-pkgs/testing.html#pytest-tests

from pyntrinio.pyntrinio import gather_financial_statement_time_series
from pytest import raises
import pandas as pd

# Sample data for testing
api_key = 'OjQ0YzljN2E4ODk5YzM1MzVhMTZmNTUwNmE2N2M0NTYz'
ticker = 'CVX'
statement = 'income_statement'
year = ['2017', '2018']
period = ['Q1', 'Q3']


def test_api_key_format():
    """
    Test if the api_key is a string
    """
    var_1=OjQ0Yz
    with raises(NameError):
        gather_financial_statement_time_series(
            var_1, ticker, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_time_series(
            123, ticker, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_time_series(
            123.3, ticker, statement, year, period)


def test_ticker_format():
    """
    Test if the ticker is a string
    """
    var_2=CVX
    with raises(NameError):
        gather_financial_statement_time_series(
            api_key, var_2, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_time_series(
            api_key, 123, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_time_series(
            api_key, 123.3, statement, year, period)


def test_output_format():
    """
    Test if the output format is of correct type ie a string ('dict' or 'pddf')
    """
    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, statement, year, period, output_format=dict)

    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, statement, year, period, output_format='pdf')


def test_year_format():
    """
    Test if the year is a list of strings and the year(s) are of length 4
    """
    var_3 = years
    with raises(Exception):
        gather_financial_statement_time_series(api_key, ticker, statement, 
            ['201', '2018'], period, output_format='pddf')

    with raises(NameError):
        gather_financial_statement_time_series(
            api_key, ticker, statement, '2017', period)

    with raises(TypeError):
        gather_financial_statement_time_series(
            api_key, ticker, statement, 2017, period)

    with raises(TypeError):
        gather_financial_statement_time_series(
            api_key, ticker, statement, 2017.0, period)

    with raises(NameError):
        gather_financial_statement_time_series(
            api_key, ticker, statement, var_3, period)

    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, statement, ['2017' '2018'], period)


def test_statement_format():
    """
    Test if the statement is a string and available in a list of valid statement options
    """
    var_4=income_statement
    with raises(NameError):
        gather_financial_statement_time_series(
            api_key, ticker, var_4, year, period)

    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, 'income_statemen', year, period)

    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, ['income_statement'], year, period)


def test_period_format():
    """
    Test if the period is a list of strings
    """
    var_5=Q1
    with raises(Exception):
        gather_financial_statement_time_series(
            api_key, ticker, 'income_statement', year, 'Q1')

    with raises(NameError):
        gather_financial_statement_time_series(
            api_key, ticker, 'income_statement', year, var_5)


def test_final_format():
    """
    Tests if the final output is of the right format
    """
    # Check that the type of the output is correct
    results = gather_financial_statement_time_series(api_key, 'AAPL',
                'income_statement', ['2018', '2019'], ['Q1'], output_format='dict')
    final_df = gather_financial_statement_time_series(api_key, 'AAPL',
                'income_statement', ['2018', '2019'], ['Q1'], output_format='pddf')
    assert(type(results) == list)
    assert(type(final_df) == pd.core.frame.DataFrame)
