# Technical part of hometask from Exness

### Structure of hometask folder
                
+ employee.py
+ test_integration.py

###### employee.py file

Contains `Employee` class that generate random and eligible parameters for POST request: name, salary and age
This class with its methods will be used in tests in file test_integration.py.

###### test_integration.py

File with tests.
3 positive and 3 negative tests. 
Some tests reuses results of previous tests. It's make the test not atomic, but they help to test some corner cases.