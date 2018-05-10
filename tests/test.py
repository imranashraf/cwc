from cwc import Worth
import logging

logging.basicConfig(format='[CWC] %(filename)-14s:%(lineno)04d %(message)s', level=logging.INFO)
myworth = Worth()
myworth.load('worth.yml')
myworth.update()
myworth.dump()
