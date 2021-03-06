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
	total_profit = current_eth_value * current_eth
	print("Profit (ETH): {:.4f} | Percent Profit: {:.2f}% | Dollar Value: ${:.2f} | Total Value ${:.2f}".format(profit, percent_profit, dollar_value, total_profit))

def current_profit_nano(current_nano, current_nano_value): #Calculate profit
	initial_invest = 26.23
	profit = current_nano - initial_invest
	percent_profit = (profit/initial_invest)*100
	dollar_value = profit*current_nano_value
	total_profit = current_nano_value * current_nano
	print("Profit (nano): {:.4f} | Percent Profit: {:.2f}% | Dollar Value: ${:.2f} | Total Value ${:.2f}".format(profit, percent_profit, dollar_value, total_profit))

def write_current_eth_value(eth_price_list):
	current_eth_value = float(input("Current ETH price: "))
	new_eth_price_list = numpy.append(eth_price_list, current_eth_value)
	print(new_eth_price_list)
	numpy.savetxt('ETH_price.csv', new_eth_price_list, delimiter = ',')
	return print('Success!!')

def current_eth_value_insys():
	eth_price_list = numpy.loadtxt('ETH_price.csv', delimiter=',')
	return eth_price_list

def save_for_day(current_eth_value, current_NANO_value):
	last_eth_value_lst = numpy.loadtxt('profit.csv', delimiter=',')
	last_eth_value = last_eth_value_lst[-1]

	current_eth_1 = float(input("Current ETH: "))
	current_eth_2 = float(input("Pool ETH: "))
	total_eth_today = current_eth_1 + current_eth_2
	profit_list = numpy.append(last_eth_value_lst, total_eth_today)
	numpy.savetxt('profit02.csv', profit_list, delimiter = ',')

	last_NANO_value_lst = numpy.loadtxt('profit02.csv', delimiter=',')
	last_NANO_value = last_NANO_value_lst[-1]

	current_NANO_1 = float(input("Current NANO: "))
	current_NANO_2 = float(input("Pool NANO: "))
	total_NANO_today = current_NANO_1 + current_NANO_2
	profit_list = numpy.append(last_NANO_value_lst, total_NANO_today)
	numpy.savetxt('profit02.csv', profit_list, delimiter = ',')

	profit_since_last = total_eth_today - last_eth_value
	dollar_value = profit_since_last*current_eth_value

	profit_since_last_2 = total_NANO_today - last_NANO_value
	dollar_value_2 = profit_since_last_2*current_NANO_value

	print("Today's Profits\n-----------------\nETH Profit: {} | Percent Profit: {} | Dollar Value: {}\nNANO Profit: {} | Percent Profit: {}  ".format(profit_since_last, (profit_since_last/last_eth_value)*100, dollar_value, profit_since_last_2, (profit_since_last_2/last_NANO_value)*100))
	
	return

def short():
	nano_amount = 1
	price = float(input("Enter price: "))
	fee = 0.01/100
	sold_eth_amnt = (nano_amount*price)*(1-fee)
	percent_buyback = float(input("Percent lower to buyback: "))
	buy_back_price = price*(1-(percent_buyback)/100)
	buyback_nano_amount = sold_eth_amnt/buy_back_price
	nano_profit = buyback_nano_amount-nano_amount 
	breakeven_price = price*(1+fee)

	print("Sell at {} | Buy back at {:6f} | Gain {:3f} Nanos | Breakeven Buyback: {}".format(price, buy_back_price, nano_profit, breakeven_price))

def main(): 
	eth_price_list = current_eth_value_insys()
	current_eth_value = eth_price_list[-1]
	current_NANO_value = 5.48
	option = int(input("1. Swingtrade | 2. Profit | 3. Enter ETH Value | 4. End of Day | 5. Short Nano | 6. Nano Profit : "))
	if option == 1: #Swingtrade
		lastprice = float(input("Buy in: "))
		delta = float(input("Percent Increase: "))
		swingit(lastprice, delta)
	elif option == 2: #Calculate Total Profits
		print('ETH PRICE: {}'.format(current_eth_value))
		current_eth_1 = float(input("Current ETH: "))
		current_eth_2 = float(input("Pool ETH: "))
		current_eth = current_eth_1+current_eth_2
		current_profit(current_eth, current_eth_value)
	elif option == 3: #Enter Current ETH Price
		current_eth_value = write_current_eth_value(eth_price_list)
	elif option == 4: #Save today's ETH Progress
		save_for_day(current_eth_value)
	elif option == 5: #Short Nano
		short()
	elif option == 6: #Nano Profit
		print('ETH PRICE: {}'.format(current_NANO_value))
		current_nano_1 = float(input("Current nano: "))
		current_nano_2 = float(input("Pool nano: "))
		current_nano = current_nano_1+current_nano_2
		current_profit_nano(current_nano, current_NANO_value)

main()
