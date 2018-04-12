import numpy
import sys

class Crypto:
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

class ETH(Crypto):
	def __init__(self):
		price_list = numpy.loadtxt('ETH_price.csv', delimiter=',')
		price = price_list[-1]
		Crypto.__init__(self, 'ETH', price)

	def save_price(self):
		price_list = numpy.loadtxt('ETH_price.csv', delimiter=',')
		price = float(input("Current ETH price: "))
		new_price_list = numpy.append(price_list, price)
		numpy.savetxt('ETH_price.csv', new_price_list, delimiter = ',')

	def __repr__(self):
		return "ETH()"

	def __str__(self):
		return "Crypto Name: {} | Price: ${}".format(self.get_name(), self.get_price())

class NANO(Crypto):
	def __init__(self):
		price_list = numpy.loadtxt('NANO_price.csv', delimiter=',')
		price = price_list[-1]
		Crypto.__init__(self, 'NANO', price)

	def save_price(self):
		price_list = numpy.loadtxt('NANO_price.csv', delimiter=',')
		price = float(input("Current NANO price: "))
		new_price_list = numpy.append(price_list, price)
		numpy.savetxt('NANO_price.csv', new_price_list, delimiter = ',')

	def __repr__(self):
		return "NANO()"

	def __str__(self):
		return "Crypto Name: {} | Price: ${}".format(self.get_name(), self.get_price())

class Action:
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
		return "Action Type: {}".format(self.get_action())

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
			breakeven_price = sell_price*(1+fee/100)
			print("Sell at {:.6f} | Buy back at {:.6f} | Gain {:.3f} Nanos | Breakeven Buyback: {:.6f}".format(sell_price, buy_back_price, profit, breakeven_price))
		except ValueError as ve:
			print("Enter valid numbers!")

	def __repr__(self):
		return "ShortIt()"

	def __str__(self):
		return "Action Type: {}".format(self.get_action())

class Calculate(Action):
	pass

class SaveForDay(Action):
	pass

def main():
	coin_list = [ETH(), NANO()]
	again = 'y'
	while again == 'y':
		while True:
			try:
				print("Main Menu\n-----------------------")
				option = int(input("1. Swing | 2. Short | 3. Profit | 4. Change Values | 5. End of Day : "))
			except ValueError as ve:
				print("Enter integers only!")
			if option == 1:
				SwingIt().action()
				break
			elif option == 2:
				ShortIt().action()
				break
			elif option == 3:
				pass
				break
			elif option == 4:
				print("Coins available:\n")
				for i in range(len(coin_list)):
					print("{}: {}\n".format(i+1, coin_list[i].get_name()))
				try:
					which_coin = int(input("Enter coin option: "))
				except ValueError as ve:
					print("Enter integers only!")
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
			elif option == 5:
				pass
				break
			elif option == 6:
				sys.exit("Quitting program...")
				break
			else:
				print("Enter a valid option: [1 to 5]")
		again = str(input("Do you want to perform another action: "))

main()

