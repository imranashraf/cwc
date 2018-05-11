from .exchange import Exchange
import logging
from ruamel import yaml
import sys

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

    def __str__(self):
        # return '' + map(str, self.exchanges) # accumulate
        worth_str = ''
        for exchange in self.exchanges:
            worth_str += str(exchange) + '\n'
        return worth_str


def main():
    logging.basicConfig(format='[CWC] %(filename)s:%(lineno)04d %(message)s', level=logging.INFO)
    logging.info('CWC: Crypto Worth Calculator')
    if len(sys.argv) < 2:
        logging.error('specify an input worth.yml file')
        sys.exit(0)

    worth_file_name = sys.argv[1]
    myworth = Worth()
    myworth.load(worth_file_name)
    myworth.update()
    myworth.dump()
    print(myworth)
