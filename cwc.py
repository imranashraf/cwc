from ruamel import yaml
from exchange import Exchange

class Worth:
    def __init__(self):
        self.total = None
        self.exchanges = []

    def load(self, fname):
        print('Lading worth')
        with open(fname, 'r') as fyml:
            for exchange_yml in yaml.safe_load(fyml)['worth']:
                exchange = Exchange()
                exchange.load(exchange_yml)
                self.exchanges.append(exchange)

    def update(self):
        print('updating worth')
        [exchange.update() for exchange in self.exchanges]

    def dump(self):
        print('Dumping worth')
        with open('worth_out.yml', 'w') as fyml:
          yaml.dump(self.exchanges, fyml, default_flow_style=False)


if __name__ == "__main__":
    myworth = Worth()
    myworth.load('worth.yml')
    myworth.update()
    myworth.dump()
