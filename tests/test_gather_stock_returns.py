# Author: Team Andrey Markov
# tests for gather_stock_returns

from pyntrinio.pyntrinio import gather_stock_returns

# helper data
api_key = 'OjhlMjhjNTBmY2IyMWJiMWE0MTExYjQwNWZmZTVkZWM1'
ticker = ['AAPL', 'CSCO']
buy_date = '2011-01-01'
sell_date = '2019-12-10'
rtn_appl = 555.38
rtn_csco = 176.01
msg1 = "Invalid Input: sell_date must be later than buy_date"
msg2 = "Invalid Date format: date must be a string in the format %Y-%m-%d"
msg3 = "Invalid API Key: please input a valid API key as a string"


def test_return_accuracy():
    """
    Test if the function correctly calculates the returns.
    """
    result = gather_stock_returns(
        api_key, ['AAPL', 'CSCO'], buy_date, sell_date)
    assert result["Return (%)"][0] == rtn_appl
    assert result["Return (%)"][1] == rtn_csco
    assert result.shape == (2, 6)


def test_api_key():
    """
    Give a wrong api_key, see if the function correctly handles the exception.
    """
    assert gather_stock_returns('abc', 'AAPL', buy_date, sell_date) == msg3


def test_date_format():
    """
    See if the function correctly handles the input dates in wrong formats.
    """
    assert gather_stock_returns(api_key, 'AAPL', '2018', sell_date) == msg2


def test_date_logic():
    """
    Exception: sell_date earlier to buy date.
    """
    assert gather_stock_returns(
        api_key, 'AAPL', buy_date='2019-01-01', sell_date='2017-01-01') == msg1
