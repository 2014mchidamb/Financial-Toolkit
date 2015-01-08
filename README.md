Financial-Toolkit
=================

A set of equity valuation tools. Thanks to StackOverflow user [Shahram](http://stackoverflow.com/questions/21565970/yahoo-finance-python-web-scraper-key-statistics-and-financial-statements) for
providing the Yahoo key statistics scraping code. 

# Generating Comps

The compgenerator.py file can be used to generate comparables for a 
list of user-specified companies. The first ticker provided must be
the ticker of the company that the others are being compared to.

```
$ python compgenerator.py
Enter a space-separated list of companies: [your company tickers here]
```
