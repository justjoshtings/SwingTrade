# SwingTrade

## About

A Crypto trading tool to calculate optimal buy/sell positions and records day-to-day profits.

## Getting Started

This program utilizes **Python3** and some common libraries/frameworks. 

Packages/frameworks needed to run on local machine:
```
- numpy
- pandas
```

### Installing

**If you already have the packages mentioned above, you can skip this section.**

I use a Mac so the following resources for installation will be Mac specific but the same idea can be applied for Windows.

**1. Install PIP**

To get Python libraries, first install **pip** or **pip3** for Python3. For new users with Macs, this [article](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) does a good job of explaining how this is done, as well as other useful tools.

Type following into terminal:

```
$ curl -O http://python-distribute.org/distribute_setup.py
$ python distribute_setup.py
```
```
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```
**2. Install Libraries**

To install Python libraries, pip (or pip3 for Python3) will be used. 

Type the following into terminal:

```
pip install numpy
```

You can substitute the name of the specific library with each one mentioned earlier until completed.

### Set Up

CSV Files Needed:

```
price.csv #Enter the current price values
profits.csv #Current profits
```

## Deployment

Run the refactored file:

Type the following into your terminal.
```
python3 swingtrade_rfctr.py
```
Follow terminal commands and you are set.

## Future Implementations

Some future implementations for this project in the works:

```
1. API Integration to get data from exchanges
2. Auto-Trading
3. More sophisticated trading algorithms
```

## Acknowledgments

I must tip my hat off to owners of any code, frameworks, media used that I do not own.

