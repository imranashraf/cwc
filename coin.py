from ruamel import yaml

class Coin:
	"""Class representing a coin"""

	def __init__(self):
		self.name = ''
		self.id = ''
		self.cost_price_eur = None
		self.cost_price_btc = None
		self.curr_price_eur = None
		self.curr_price_btc = None
		self.change = None

	def print(self):
		print('{} {}'.format(self.name, self.id) )
		print('    cost_price_eur : {}'.format(self.cost_price_eur) )
		print('    cost_price_btc : {}'.format(self.cost_price_btc) )
		print('    curr_price_eur : {}'.format(self.curr_price_eur) )
		print('    curr_price_btc : {}'.format(self.curr_price_btc) )


class Coins:
	""" list of coins """

	def __init__(self):
		self.coins = []

	def load(self):
		print('Loading coins')
		with open("coins.yml", 'r') as fyml:
			for coin_yml in yaml.safe_load(fyml)['coins']:
				coin = Coin()
				coin.name = coin_yml['name']
				coin.name = coin_yml['id']
				coin.cost_price_btc = coin_yml['cost_price_btc']
				coin.cost_price_eur = coin_yml['cost_price_eur']
				self.coins.append(coin)


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
	myCoins.print()
	myCoins.dump()

