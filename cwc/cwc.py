from .exchange import Exchange
import logging
from ruamel import yaml

class Worth:
    def __init__(self):
        self.total = None
        self.exchanges = []

    def load(self, fname):
        logging.info('Lading worth')
        with open(fname, 'r') as fyml:
            for exchange_yml in yaml.safe_load(fyml)['worth']:
                exchange = Exchange()
                exchange.load(exchange_yml)
                self.exchanges.append(exchange)

    def update(self):
        logging.info('updating worth')
        [exchange.update() for exchange in self.exchanges]

    def dump(self):
        logging.info('Dumping worth')
        with open('worth_out.yml', 'w') as fyml:
          yaml.dump(self.exchanges, fyml, default_flow_style=False)


if __name__ == "__main__":
    logging.basicConfig(format='[CWC] %(filename)-14s:%(lineno)04d %(message)s', level=logging.INFO)
    myworth = Worth()
    myworth.load('../tests/worth.yml')
    myworth.update()
    myworth.dump()
