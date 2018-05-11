import json, requests
import logging

class Price:

	def __init__(self, amt=0, curr=None):
		self.amount = amt
		self.currency = curr

	def __str__(self):
		return '{0:.10f} {1}'.format(self.amount, self.currency)


class Coin:
	"""Class representing a coin"""

	def __init__(self):
		self.name = None
		self.symbol = None
		self.amount = None
		self.cost_price = None
		self.curr_price = None
		self.percent_change = None
		# self.percent_change_btc_total = None
		# self.percent_change_btc_1h = None
		# self.percent_change_btc_24h = None

	def load(self, coin_yml):
		logging.debug('Loading a coin')
		try:
			self.name = coin_yml['name']
			self.amount = coin_yml['amount']
			cp = coin_yml['cost_price'].split()
			self.cost_price = Price(float(cp[0]), cp[1])
		except:
			logging.error('Improper specification of coin in yaml file!')
			pass

	def update(self):
		try:
			currency = self.cost_price.currency
			json_response = requests.get('https://api.coinmarketcap.com/v1/ticker/'+ self.name + '/?convert=' + currency).json()[0]
			self.symbol = json_response['symbol']
			self.curr_price = Price(float(json_response["price_" + currency]), currency)
			self.percent_change = (self.curr_price.amount - self.cost_price.amount)/self.cost_price.amount * 100.0
			# self.percent_change_btc_1h = float(json_response["percent_change_1h"])
			# self.percent_change_btc_24h = float(json_response["percent_change_24h"])
		except:
			logging.error('Error updating current price of {}'.format(self.name))
			pass

	# def __str__(self):
	# 	str_coin = '{} ({})\n'.format(self.name, self.symbol)
	# 	str_coin +='    amount : {}\n'.format(self.amount)
	# 	str_coin +='    cost_price : {}\n'.format(str(self.cost_price))
	# 	str_coin +='    curr_price : {}\n'.format(str(self.curr_price))
	# 	str_coin +='    percent_change : {0:.1f}\n'.format(self.percent_change)
	# 	return str_coin

	def __str__(self):
		nsym = self.name+'('+self.symbol+')'
		str_coin = '{0:20} {1:>9.3f}   {2:^18}   {3:^18}   {4:.1f}%'.format(nsym, self.amount,
			str(self.cost_price), str(self.curr_price), self.percent_change)
		return str_coin
