from pyntrinio import pyntrinio

def test_gather_financial_statement_company_compare():
    '''
    Tests if the inputs are the right type, if the output has one value that we expect
    ''' 
    api_key = 'OmEzNGY3MGEwMDIwZGM5Y2UxNDZhNzUzMTgzYTJiNWI2'
    ticker = ['AAPL', 'CSCO']
    statement = 'income_statement'
    year = '2014'
    period = 'Q1'
    result_dic = gather_financial_statement_company_compare(api_key, ticker, statement, year, period, output_format='dict')
    result_df = gather_financial_statement_company_compare(api_key, ticker, statement, year, period, output_format='pddf')

    #Check that the number of rows of the dataframe corresponds to the number of companies
    assert(len(result_dic) == 2)
   
    #Check that the type of the output is the right one
    assert(type(result_dic) == list)
    assert(type(result_df) == pd.core.frame.DataFrame)
   
    #Check that when the api_key is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(['la'], ticker, statement, year, period)
    
    #Check that when the statement is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(api_key, ticker, 123, year, period)
    
    #Check that when the year is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(api_key, ticker, statement, 1954, period)
    
    #Check that when the period is not a string, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(api_key, ticker, statement, year, 3)
    
    #Check that when the ticker is not a list, it returns an error
    with raises(TypeError):
        gather_financial_statement_company_compare(api_key, 'AAPL', statement, year, period)
    
    #Check that when the year is not of length 4, it returns an error
    with raises(Exception):
        gather_financial_statement_company_compare(api_key, ticker, statement, '97', period)
    
    #Check that the first dictionnary of the output has a key 'ticker' and that its value correspond to ticker
    assert(result_dic[0]['ticker'] == ticker[0])