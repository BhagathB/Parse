import json
import urllib
from urllib.request import urlopen

with urlopen('http://finance.google.com/finance/info?client=ig&q=NASDAQ%3AAAPL,GOOG') as story:
    for line in story:
        line = line.decode('utf-8')
        print(line)


