# Telecom call billing system

#### Excersice

A company like AT&T wants to have a simple system for call billing.

Call plans:
- weekend call costs 0.01 $ per minute
- late night calls costs 0.02 $ per minute
- regular calls costs 0.05 $ per minute

For those clients that are new, a discount is given, they can pay the same rate as late night calls for the regular ones.
Those existing clients will pay the rates from the call plans.

Business Rule: If a call is international the rate will be doubled.

Goal: The company would like to have a basic billing system to calculate the total charge of every call history from any client.

Use OOP and test the code.

#### Description
This is a project to generate the billing from a telecom company. The idea was to write the code using Object-oriented programming (OOP) in order to apply hierarchy and polymorphism to make a more reusable and testable code.
Unit Tests were applied in this project to check the system under normal conditions and under wrong conditions as well. In that way we can know if the exception are properly set and we can also check the desirable output.
As this project does not use any external library the requirements.txt file was not neccesary.

#### Installation
The only requirement is to have Python 3.

#### Usage
##### Windows 7/8/10
After unzipping the file, inside the directory you have to press: <kbd>SHIFT</kbd> + Right Click and then press "Open console here. Then you have to type the following command in the console:
```console
python -m unittest unit_tests.py
```
##### Linux
After unzipping the file, inside the directory you have to open a console: Then you have to type the following command in the console:
```console
python3 -m unittest unit_tests.py
```

### Test Coverage

**Results in coveralls**

[![Coverage Status](https://coveralls.io/repos/github/yaritaft/call_billing/badge.svg?branch=master)](https://coveralls.io/github/yaritaft/call_billing?branch=master)


### Technology

#### Programming Language

Python version 3.7.0

#### Dependencies 
`coverage==4.5.4`

Dependencies can also be found in requirements.txt.

### Standards

- Google Python Style Guide: http://google.github.io/styleguide/pyguide.html


### Author
Yari Ivan Taft

https://github.com/yaritaft/
