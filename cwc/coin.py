import json, requests
import logging

class Coin:
	"""Class representing a coin"""

	def __init__(self):
		self.name = None
		self.symbol = None
		self.amount = None
		self.cost_price_eur = None
		self.cost_price_btc = None
		self.curr_price_eur = None
		self.curr_price_btc = None
		self.percent_change_eur_total = None
		self.percent_change_btc_total = None
		self.percent_change_btc_1h = None
		self.percent_change_btc_24h = None

	def load(self, coin_yml):
		logging.info('Loading a coin')
		try:
			self.name = coin_yml['name']
			self.symbol = coin_yml['symbol']
			self.amount = coin_yml['amount']
			self.cost_price_btc = coin_yml['cost_price_btc']
			self.cost_price_eur = coin_yml['cost_price_eur']
		except:
			logging.error('Improper specification of coin in yaml file!')
			pass

	def update(self):
		currency = 'eur'
		coin = self.name
		try:
			json_response = requests.get('https://api.coinmarketcap.com/v1/ticker/'+ coin + '/?convert=' + currency).json()[0]
			self.curr_price_eur = float(json_response["price_" + currency])
			self.curr_price_btc = float(json_response["price_" + 'btc'])
			self.percent_change_btc_1h = float(json_response["percent_change_1h"])
			self.percent_change_btc_24h = float(json_response["percent_change_24h"])
			self.percent_change_eur_total = (self.curr_price_eur - self.cost_price_eur)/self.cost_price_eur * 100.0
			self.percent_change_btc_total = (self.curr_price_btc - self.cost_price_btc)/self.cost_price_btc * 100.0
		except:
			logging.error('Error updating current price of {}'.format(self.name))
			pass

	def __str__(self):
		str_coin = '{} ({})\n'.format(self.name, self.symbol)
		str_coin +='    amount : {}\n'.format(self.amount)
		str_coin +='    cost_price_eur : {0:.10f}\n'.format(self.cost_price_eur)
		str_coin +='    cost_price_btc : {0:.10f}\n'.format(self.cost_price_btc)
		str_coin +='    curr_price_eur : {0:.10f}\n'.format(self.curr_price_eur)
		str_coin +='    curr_price_btc : {0:.10f}\n'.format(self.curr_price_btc)
		str_coin +='    percent_change_eur_total : {0:.1f}\n'.format(self.percent_change_eur_total)
		str_coin +='    percent_change_btc_total : {0:.1f}\n'.format(self.percent_change_btc_total)
		return str_coin
