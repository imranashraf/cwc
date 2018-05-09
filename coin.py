import json, requests
from ruamel import yaml

class Coin:
	"""Class representing a coin"""

	def __init__(self):
		self.name = ''
		self.symbol = ''
		self.cost_price_eur = None
		self.cost_price_btc = None
		self.curr_price_eur = None
		self.curr_price_btc = None
		self.percent_change_eur_total = None
		self.percent_change_btc_total = None
		self.percent_change_btc_1h = None
		self.percent_change_btc_24h = None

	def update_curr_price(self):
		currency = 'eur'
		coin = self.name
		try:
			rj = requests.get('https://api.coinmarketcap.com/v1/ticker/'+ coin + '/?convert=' + currency).json()[0]
			self.curr_price_eur = float(rj["price_" + currency])
			self.curr_price_btc = float(rj["price_" + 'btc'])
			self.percent_change_btc_1h = float(rj["percent_change_1h"])
			self.percent_change_btc_24h = float(rj["percent_change_24h"])
			self.percent_change_eur_total = (self.curr_price_eur - self.cost_price_eur)/self.cost_price_eur * 100.0
			self.percent_change_btc_total = (self.curr_price_btc - self.cost_price_btc)/self.cost_price_btc * 100.0
		except:
			print('Error updating current price of {}'.format(self.name))


	def print(self):
		print('{} {}'.format(self.name, self.symbol) )
		print('    cost_price_eur : {}'.format(self.cost_price_eur) )
		print('    cost_price_btc : {}'.format(self.cost_price_btc) )
		print('    curr_price_eur : {}'.format(self.curr_price_eur) )
		print('    curr_price_btc : {}'.format(self.curr_price_btc) )
		print('    percent_change_eur_total : {}'.format(self.percent_change_eur_total) )
		print('    percent_change_btc_total : {}'.format(self.percent_change_btc_total) )


class Coins:
	""" list of coins """

	def __init__(self):
		self.coins = []

	def load(self):
		print('Loading coins')
		with open("coins.yml", 'r') as fyml:
			for coin_yml in yaml.safe_load(fyml)['coins']:
				try:
					coin = Coin()
					coin.name = coin_yml['name']
					coin.symbol = coin_yml['symbol']
					coin.cost_price_btc = coin_yml['cost_price_btc']
					coin.cost_price_eur = coin_yml['cost_price_eur']
					self.coins.append(coin)
				except:
					print('Improper specification of coin in yaml file!')

	def update_curr_price(self):
		print('Updating current price of coins:')
		for coin in self.coins:
			coin.update_curr_price()


	def print(self):
		print('Printing coins:')
		for coin in self.coins:
			coin.print()

	def dump(self):
		print('Dumping coins')
		with open('coins_out.yml', 'w') as fyml:
			yaml.dump(self.coins, fyml, default_flow_style=False)

myCoins = Coins()
if __name__ == "__main__":
	myCoins.load()
	myCoins.update_curr_price()
	myCoins.print()
	myCoins.dump()

