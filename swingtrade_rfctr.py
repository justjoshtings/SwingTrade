import numpy as np
import sys
import pandas as pd

class Crypto: #Class: 'Crypto' | Has methods: set_name, get_name, set_price, get_price
	def __init__(self, name, price):
		self.__name = name
		self.__price = price

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_price(self, price):
		self.__price = price

	def get_price(self):
		return self.__price

	def __repr__(self):
		return "Crypto('{}', '{}')".format(self.__name, self.__price)

	def __str__(self):
		return "Crypto Name: {} | Price: {}".format(self.__name, self.__price)

class ETH(Crypto): #Subclass of 'Crypto': 'ETH' | Has methods: save_price
	def __init__(self):
		self.__price_list = np.loadtxt('ETH_price.csv', delimiter=',')
		self.__price = self.__price_list[-1]
		Crypto.__init__(self, 'ETH', self.__price)

	def save_price(self):
		self.__price_list = np.loadtxt('ETH_price.csv', delimiter=',')
		self.__price = float(input("Current ETH price: "))
		self.__new_price_list = np.append(self.__price_list, self.__price)
		np.savetxt('ETH_price.csv', self.__new_price_list, delimiter = ',')

	def __repr__(self):
		return "ETH()"

	def __str__(self):
		return "Crypto Name: {} | Price: ${} | Has Methods: 'save_price()'".format(self.get_name(), self.get_price())

class NANO(Crypto): #Subclass of 'Crypto': 'NANO' | Has methods: save_price
	def __init__(self):
		self.__price_list = np.loadtxt('NANO_price.csv', delimiter=',')
		self.__price = self.__price_list[-1]
		Crypto.__init__(self, 'NANO', self.__price)

	def save_price(self):
		self.__price_list = np.loadtxt('NANO_price.csv', delimiter=',')
		self.__price = float(input("Current NANO price: "))
		self.__new_price_list = np.append(self.__price_list, self.__price)
		np.savetxt('NANO_price.csv', self.__new_price_list, delimiter = ',')

	def __repr__(self):
		return "NANO()"

	def __str__(self):
		return "Crypto Name: {} | Price: ${} | Has Methods: 'save_price()'".format(self.get_name(), self.get_price())

class Action: #Class: 'Action' | Has methods: set_action, get_action
	def __init__(self, action_type):
		self.__action_type = action_type

	def set_action(self, action_type):
		self.__action_type = action_type

	def get_action(self):
		return self.__action_type

	def __repr__(self):
		return "Action('{}')".format(self.__action_type)

	def __str__(self):
		return "Action Type: {}".format(self.__action_type)

class SwingIt(Action):
	def __init__(self):
		Action.__init__(self, 'SwingIt')

	def action(self):
		fee = 0.1
		try: 
			buy_in_price = float(input("Buy In Price: "))
			percent_delta = float(input("Percent Incrase: "))
			target_price = buy_in_price * (1+(percent_delta/100))
			breakeven = buy_in_price*(1+(fee/100))
			print("Buy In:{:.6f} | Percent Increase:{:.2f}%".format(buy_in_price, percent_delta))
			print("Target Price:{:.6f} | Breakeven Price: {:.6f}".format(target_price, breakeven))
		except ValueError as ve:
			print("Enter valid numbers")

	def __repr__(self):
		return "SwingIt()"

	def __str__(self):
		return "Action Type: {} | Has Methods: 'action()'".format(self.get_action())

class ShortIt(Action):
	def __init__(self):
		Action.__init__(self, 'ShortIt')

	def action(self):
		fee = 0.1
		try:
			sell_price = float(input("Sell Price: "))
			percent_delta = float(input("Percent Decrease: "))
			amount = float(input("Amount Sold: "))
			sold_amt = (amount*sell_price)*(1-fee/100)
			buy_back_price = sell_price*(1-(percent_delta)/100)
			buy_back_amt = sold_amt/buy_back_price
			profit = buy_back_amt - amount
			breakeven_price = sell_price*(1-fee/100)
			print("Sell at {:.6f} | Buy back at {:.6f} | Gain {:.3f} Nanos | Breakeven Buyback: {:.6f}".format(sell_price, buy_back_price, profit, breakeven_price))
		except ValueError as ve:
			print("Enter valid numbers!")

	def __repr__(self):
		return "ShortIt()"

	def __str__(self):
		return "Action Type: {} | Has Methods: 'action()'".format(self.get_action())

class Calculate(Action):
	def __init__(self, which_coin, initial_value, price):
		Action.__init__(self, 'Calculate')
		self.__which_coin = which_coin
		self.__initial_value = initial_value
		self.__price = price

	def set_initial(self, initial_value):
		self.__initial_value = initial_value

	def get_initial(self):
		return self.__initial_value

	def set_price(self):
		self.__price = price

	def get_price(self):
		return self.__price

	def set_coin_name(self):
		self.__which_coin = which_coin

	def get_coin_name(self, which_coin):
		self.__coin_name = ''
		if which_coin == 1:
			self.__coin_name = 'ETH'
			return self.__coin_name
		elif which_coin == 2:
			self.__coin_name = 'NANO'
			return self.__coin_name

	def calculating(self):
		self.__coin_amt = float(input("Enter coin amount: "))
		self.__coin_amt_pool  = float(input("Enter pool amount: "))
		print("Calculating profits...")
		self.__current_total = self.__coin_amt + self.__coin_amt_pool
		self.__current_profit = self.__current_total - float(self.__initial_value)
		self.__percent_profit = (self.__current_profit/float(self.__initial_value))*100
		self.__dollar_profit_value = self.__percent_profit * self.__price
		self.__dollar_total_value = self.__current_total * self.__price
		print("Profit ({}): {:.6f} | Percent Profit: {:.2f}% | Dollar Value: ${:.2f} | Total Dollar Value ${:.2f}".format(self.get_coin_name(self.__which_coin), self.__current_profit, self.__percent_profit, self.__dollar_profit_value, self.__dollar_total_value))

	def __repr__(self):
		return "Calculate()"

	def __str__(self):
		return "Action Type: {} | Coin Name: {} | Initial Amount: {:.6f} | Has Methods: 'get_coin_name('which_coin')', calculating('which_coin', 'initial_value')".format(self.get_action(), self.get_coin_name(), self.get_initial(),)

class ChooseCoin(Action):
	def __init__(self):
		Action.__init__(self, 'ChooseCoin')

	def set_coin_list(self, coin_list):
		self.__coin_list = coin_list

	def get_coin_list(self):
		return self.__coin_list

	def choosing(self, coin_list):
		self.__coin_list = coin_list
		print("Coins available:\n")
		for i in range(len(self.__coin_list)):
			print("{}: {}\n".format(i+1, self.__coin_list[i].get_name()))
		try:
			self.__which_coin = int(input("Enter coin option: "))
		except ValueError as ve:
			print("Enter integers only!")
		return self.__which_coin

	def __repr__(self):
		return "ChooseCoin()"

	def __str__(self):
		return "Action Type: {} | Coins List: {} | Has Methods: 'choosing('coin_list')'".format(self.get_action(), self.get_coin_list())

class GetInitial(Action):
	def __init__(self):
		Action.__init__(self, 'GetInitial')

	#Setting initial values into a dict, then into a dataframe and saving into a .csv file
	def saving_initial(self): 
		initials = {'ETH': [0.363346, ], 'NANO': [26.23, ]}
		df = pd.DataFrame(data = initials)
		try: 
			df.to_csv('initials.csv', encoding = 'utf-8', index = False)
		except IOError:
			print("Error saving initial values to 'initials.csv'")

	def changing_initial(self):
		while True:
			try:
				change_values = str(input("Do you want to change initial values? (y/n): "))
				if change_values == 'y':
					while True:
						try:
							self.__coin = int(input("Which coin do you want to change?\n1. ETH | 2. NANO : "))
							if self.__coin == 1:
								try:
									new_initial_amt = float(input("New initial amount for ETH: "))					
									initials = {'ETH': [new_initial_amt, ], 'NANO': [26.23, ]}
									df = pd.DataFrame(data = initials)
									df.to_csv('initials.csv', encoding = 'utf-8', index = False)
									print("Values Changed")
								except ValueError as ve:
									print("Enter a valid number!")
								except IOError:
									print("Error saving initial values to 'initials.csv'")
								break
							elif self.__coin == 2:
								try:
									new_initial_amt = float(input("New initial amount for NANO: "))				
									initials = {'ETH': [0.363346, ], 'NANO': [new_initial_amt, ]}
									df = pd.DataFrame(data = initials)
									df.to_csv('initials.csv', encoding = 'utf-8', index = False)
									print("Values Changed")
								except ValueError as ve:
									print("Enter a valid number!")
								except IOError:
									print("Error saving initial values to 'initials.csv'")
								break
							else:
								print("Please enter a valid choice!")
						except ValueError as ve:
							print("Please enter a number")
				elif change_values == 'n':
					print("No changes")
					break
				else:
					print("Enter only 'y' or 'n'!")
			except ValueError as ve:
				print("Enter 'y' or 'n'!")
		
	def getting_initial(self, coin_choice):
		self.__coin_choice = coin_choice
		try:
			df = pd.read_csv('initials.csv', header = None)
			pass
		except IOError:
			print("Error opening initial values from 'initials.csv'")
		if self.__coin_choice == 1:
			try:
				initial_value = df.loc[1][0]
				return initial_value
			except NameError:
				print("File: 'initials.csv' did not load properly")
		elif self.__coin_choice == 2:
			try:
				initial_value = df.loc[1][1]
				return initial_value
			except NameError:
				print("File: 'initials.csv' did not load properly")

	def __repr__(self):
		return "GetInitial()"

	def __str__(self):
		return "Action Type: {} | Has Methods: 'saving_initial()', 'changing_initial()', 'getting_initial()'".format(self.get_action())

class SaveForDay(Action):
	def __init__(self):
		Action.__init__(self, 'SaveForDay')

	def saving(self): #Choose which coin to input and calculate profits based on last entry
		pass

#If need to add new coin:
	#1. Add new coin subclass
	#2. Add subclass to list
	#3. Update GetInitial class
	#4. Add additional 'initial_value_coin' values
	
def main():
	coin_list = [ETH(), NANO()] #Current coin list, add additional ones as needed
	again = 'y'
	while again == 'y':
		while True:
			try:
				print("Main Menu\n-----------------------")
				option = int(input("1. Swing | 2. Short | 3. Profit | 4. Change Price Values | 5. End of Day | 6. Change Initial Values: "))
			except ValueError as ve:
				print("Enter integers only!")
			if option == 1: #Calculate swing trade positions
				SwingIt().action()
				break
			elif option == 2: #Calculate short positions
				ShortIt().action()
				break
			elif option == 3: #Option to calculate profits
				which_coin = ChooseCoin().choosing(coin_list)
				if which_coin == 1:
					price = ETH().get_price()
				elif which_coin == 2:
					price = NANO().get_price()
				initial_value = GetInitial().getting_initial(which_coin)
				try:
					Calculate(which_coin, initial_value, price).calculating()
				except NameError:
					print("Error in getting price!")
				break
			elif option == 4: #Option to change current coin/USD pairing values
				which_coin = ChooseCoin().choosing(coin_list)
				while True:
					if which_coin == 1:
						print(coin_list[0])
						coin_list[0].save_price()
						coin_list[0] = ETH()
						print(coin_list[0])
						break
					elif which_coin == 2:
						print(coin_list[1])
						coin_list[1].save_price()
						coin_list[1] = NANO()
						print(coin_list[1])
						break
					else:
						print("Enter a valid option!")
			elif option == 5: #Option to enter end of day progress to track daily progress
				pass
				break
			elif option == 6: #Change initial investment value amounts
				GetInitial().changing_initial()
				break
			elif option == 7: #Quit program
				sys.exit("Quitting program...")
				break
			else:
				print("Enter a valid option: [1 to 5]")
		again = str(input("Do you want to perform another action: "))

main()


