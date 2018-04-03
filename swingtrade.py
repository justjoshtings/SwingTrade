
import os
from numpy import genfromtxt
import numpy

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| pbcopy'
    os.system(command)

def swingit(lastprice, delta): #Calculate swing prices
	newprice = lastprice * (1+(delta/100))
	breakeven = lastprice*(1+(0.1/100))
	print("Buy In:{} | Percent Increase:{}%".format(lastprice, delta))
	print("Target Price:{} | Breakeven Price: {}".format(newprice, breakeven))
	addToClipBoard(str(newprice))
	return

def current_profit(current_eth, current_eth_value): #Calculate profit
	initial_invest = 0.1062365+0.00133461+0.25577442
	profit = current_eth - initial_invest
	percent_profit = (profit/initial_invest)*100
	dollar_value = profit*current_eth_value
	print("Profit (ETH): {} | Percent Profit: {} | Dollar Value: {}".format(profit, percent_profit, dollar_value))

def write_current_eth_value(eth_price_list):
	current_eth_value = float(input("Current ETH price: "))
	new_eth_price_list = numpy.append(eth_price_list, current_eth_value)
	print(new_eth_price_list)
	numpy.savetxt('ETH_price.csv', new_eth_price_list, delimiter = ',')
	return print("Sucess!")

def current_eth_value_insys():
	eth_price_list = numpy.loadtxt('ETH_price.csv', delimiter=',')
	return eth_price_list
	

def main(): 
	eth_price_list = current_eth_value_insys()
	current_eth_value = eth_price_list[-1]
	option = int(input("Swingtrade or Profit or Enter ETH Value?\n1 or 2 or 3: "))
	if option == 1:
		lastprice = float(input("Buy in: "))
		delta = float(input("Percent Increase: "))
		swingit(lastprice, delta)
	elif option == 2:
		print('ETH PRICE: {}'.format(current_eth_value))
		current_eth_1 = float(input("Current ETH: "))
		current_eth_2 = float(input("Pool ETH: "))
		current_eth = current_eth_1+current_eth_2
		current_profit(current_eth, current_eth_value)
	elif option == 3:
		current_eth_value = write_current_eth_value(eth_price_list)
		

main()

