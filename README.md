## pyntrinio 

![](https://github.com/UBC-MDS/pyntrinio/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyntrinio/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyntrinio) ![Release](https://github.com/UBC-MDS/pyntrinio/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pyntrinio/badge/?version=latest)](https://pyntrinio.readthedocs.io/en/latest/?badge=latest)

Python package converts Intrinio objects to native python and pandas objects.

### The Project
This project has been created as part of [UBC's Master of Data Science Program](https://masterdatascience.ubc.ca/). Information about the contributors can be found [here](CONTRIBUTORS.md). The Code of Conduct can be found [here](CONDUCT.md). The collaboration expectations regarding use of Github Flow can be found [here](CONTRIBUTING.md).

If you were to search the web for "historical stock data", or "financial statement data", the results you would come across would be a variety of web applications (such as Google Finance), and maybe some PDFs of financial statements. This is fair, as there is a massive volume of stock data, and financial statements require lots of discretion (including standards followed - US companies may choose between reporting under IFRS and US GAAP). [Intrinio](https://intrinio.com/) offers solutions to this problem with an API platform that can easily be used to extract data and perform further analysis on it.

Intrinio is an excellent source to get data into a python environment to analyse data, but a problem persists that the data can't be directly analysed from Intrinio objects. That is where pytrinio comes in. This package will offer a variety of functions that allow users to seamlessly transform Intrinio objects into either python dictionaries or a pandas dataframe. This will enable users of the data to make the most of Intrinio's reliable and easy-to-use API platform, as well as the analysis capabilities that are available in python's environment.

### pytrinio in the Python Ecosystem
Python is an object-oriented programming language, which has allowed contributors of packages to make complex data types appear simple, and overall make packages easy for users to use. This has led to the popularity of some objects, such as numpy and pandas objects. These have been widely accepted and are key structures in the python environment. Most objects however, are not integrated with packages the same way that numpy and pandas have been adopted. This means that generally users will need to change the data type of objects either native python object types (such as dictionaries or lists), or to a widely accepted object. The goal of this project is to make stock and financial statement data more accessible by translating the objects into dictionaries or pandas objects (user's choice) so that the end user can focus on analysis and drawing insights from the data.

### Installation:

```
pip install -i https://test.pypi.org/simple/ pyntrinio
```

### Features
- TODO

### Functions
1. **gather_financial_statement_time_series()**: This function takes in a single stock ticker symbol, the statement, the year, and a list of various periods to compare, and a string specifying if we want the output as a dictionnary or a data frame. It returns a table or a data frame (depending on the input) of the information in the selected statement, fora time-series analysis of the company specified.
2. **gather_financial_statement_company_compare()**: This function takes in a list containing the tickers of the companies we want to compare, the statement, the year and the period of the year we want to study, and a string specifying if we want the output as a dictionnary or a data frame. It returns a table or a data frame (depending on the input) of the information in the selected statement, for the selected companies at the wanted time. 
3. **gather_stock_time_series()**: This function takes in a single stock ticker symbol and returns historical stock price data from a timeframe, returned as a dictionary or a pandas dataframe depending on specification.
4. **gather_stock_returns()**: This function takes in multiple stock ticker symbols, buy-in date, sell-out date and returns a dataframe containing the historical prices at buy-in and sell-out date as well as the corresponding returns (profit/loss).

### Dependencies

Before using any functions included in this package, you must sign up for an appropriate [Intrinio account](https://intrinio.com/). Once you have signed up for the appropriate account, you can find your API key (which is a required argument in all functions) by doing the following:

1. In the top right corner, select `My Account`
2. In the left hand menu, select `API KEYS`
3. Copy your relevant API Key. Note that this is unique to you and should not be shared.


- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://pyntrinio.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### References
(2007). Retrieved from intrinio.com
