from .coin import Coin
import logging

class Exchange:
    def __init__(self):
        self.name = None
        self.coins = []

    def load(self, exchange_yml):
        logging.info('loading an exchange')
        try:
            self.name = exchange_yml['exchange_name']
        except:
            logging.error('Could not get exchange name')
            pass

        for coin_yml in exchange_yml['coins']:
            coin = Coin()
            coin.load(coin_yml)
            self.coins.append(coin)

    def update(self):
        [coin.update() for coin in self.coins]

    def __str__(self):
        ex_str = self.name + '\n'
        for coin in  self.coins:
            ex_str += str(coin)
        return ex_str