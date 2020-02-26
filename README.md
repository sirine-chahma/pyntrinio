## pyntrinio 

![](https://github.com/UBC-MDS/pyntrinio/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyntrinio/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyntrinio) ![Release](https://github.com/UBC-MDS/pyntrinio/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pyntrinio/badge/?version=latest)](https://pyntrinio.readthedocs.io/en/latest/?badge=latest)

Python package converts Intrinio objects to native python and pandas objects.

### The Project
This project has been created as part of [UBC's Master of Data Science Program](https://masterdatascience.ubc.ca/). Information about the contributors can be found here **link to CONTRIBUTORS.md**. The Code of Conduct can be found here **link to CONDUCT.md**. The collaboration expectations regarding use of Github Flow can be found here **link to CONTRIBUTING.md**.

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

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://pyntrinio.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
