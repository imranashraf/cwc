from .coin import Coin
import logging

class Exchange:
    def __init__(self):
        self.name = None
        self.coins = []

    def load(self, exchange_yml):
        logging.debug('loading an exchange')
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
        header = '{0:20} {1:^12} {2:^18} {3:^18} {4:^12}\n'.format('Name(Symbol)', 'Amount', 'Cost Price', 'Curr Price', 'Change(%)')
        ex_str = '\n{0:^80}\n'.format(self.name+' exchange')
        ex_str += header
        for coin in  self.coins:
            ex_str += str(coin) + '\n'
        return ex_str