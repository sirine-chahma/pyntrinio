# Author: Team Andrey Markov
# tests for gather_financial_statement_company_compare

from pyntrinio.pyntrinio import gather_financial_statement_company_compare
from pytest import raises
import pandas as pd
"""
This script tests the gather_financial_statement_company_compare functions 
in the pyntrinio module.
"""


def test_type_input():
    '''
    Tests if the types of the inputs are the right ones
    '''
    api_key = 'OmEzNGY3MGEwMDIwZGM5Y2UxNDZhNzUzMTgzYTJiNWI2'
    ticker = ['AAPL', 'CSCO']
    statement = 'income_statement'
    year = '2014'
    period = 'Q1'

    # Check that when the api_key is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(
            ['la'], ticker, statement, year, period)
    with raises(NameError):
        gather_financial_statement_company_compare(
            la, ticker, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(123, ticker, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(123.3, ticker, statement, year, period)

    # Check that when the statement is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, 123, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, 123.3, year, period)
    with raises(NameError):
        gather_financial_statement_company_compare(
            api_key, ticker, stat, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, ['stat'], year, period)

    # Check that when the year is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, 1954, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, 1954.4, period)
    with raises(NameError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, years, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
        api_key, ticker, statement, ['123'], period)

    # Check that when the period is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, year, 3)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, year, 3.3)
    with raises(NameError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, year, periods)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, year, ['3.3'])

    # Check that when the ticker is not a list, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, 'AAPL', statement, year, period)
    with raises(NameError):
        gather_financial_statement_company_compare(
            api_key, AAPL, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, 123, statement, year, period)
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, 123.3, statement, year, period)

    # Check if the ticker is a list of strings
    with raises(TypeError):
        gather_financial_statement_company_compare(
            api_key, ['AAPL', 123], statement, year, period)

    # Check if the statement is valid
    with raises(Exception):
        gather_financial_statement_company_compare(
            api_key, ticker, 'a_statement', year, period)

    # Check is the output format is valid
    with raises(Exception):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, year, period, output_format='output')

    # Check if the API key is correct
    msg = "Invalid API Key: please input a valid API key as a string"
    assert gather_financial_statement_company_compare(
        'wrong_key', ticker, statement, year, period) == msg

    # Check the the arguments are right
    msg = "Invalid agruments: please make sure that your statement\
        /year/period are valid"
    assert gather_financial_statement_company_compare(
        api_key, ['ticker'], statement, year, period) == msg


def test_output():
    '''
    Tests if the output seems right (type, dimension and one value)
    ''' 
    api_key = 'OmEzNGY3MGEwMDIwZGM5Y2UxNDZhNzUzMTgzYTJiNWI2'
    ticker = ['AAPL', 'CSCO', 'CAT', 'AXP', 'IBM']
    statement = 'income_statement'
    year = '2014'
    period = 'Q1'
    result_dic = gather_financial_statement_company_compare(
        api_key, ticker, statement, year, period, output_format='dict')
    result_df = gather_financial_statement_company_compare(
        api_key, ticker, statement, year, period, output_format='pddf')

    # Check that the type of the output is the right one
    assert(type(result_dic) == list)
    assert(type(result_df) == pd.core.frame.DataFrame)

    # Check that the first dictionnary of the output has a key
    # 'ticker' and that its value correspond to ticker
    assert(result_dic[0]['ticker'] == ticker[0])

    # Check that the number of rows of the dataframe corresponds
    # to the number of companies
    assert(len(result_dic) == 5)


def test_year():
    '''
    Tests if the length of year is 4
    ''' 
    api_key = 'OmEzNGY3MGEwMDIwZGM5Y2UxNDZhNzUzMTgzYTJiNWI2'
    ticker = ['AAPL', 'CSCO']
    statement = 'income_statement'
    period = 'Q1' 

    # Check that when the year is not of length 4, it returns an error
    with raises(Exception):
        gather_financial_statement_company_compare(
            api_key, ticker, statement, '97', period)