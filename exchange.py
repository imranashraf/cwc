from coin import Coin

class Exchange:
    def __init__(self):
        self.name = None
        self.coins = []

    def load(self, exchange_yml):
        print('loading an exchange')
        try:
            self.name = exchange_yml['exchange_name']
        except:
            pass

        for coin_yml in exchange_yml['coins']:
            coin = Coin()
            coin.load(coin_yml)
            self.coins.append(coin)

    def update(self):
        [coin.update() for coin in self.coins]
