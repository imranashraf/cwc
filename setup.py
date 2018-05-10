import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='cwc',
      version='0.0.1',
      description='CWC: Crypto Worth Calcultor',
      long_description=read('README.md'),
      author='Imran Ashraf',
      author_email='nader.khammassi@gmail.com, iimran.aashraf@gmail.com',
      url="https://github.com/imranashraf/cwc",
      packages=['cwc'],
      zip_safe=False)
