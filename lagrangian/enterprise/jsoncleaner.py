import urllib
import re
import json
import time
import math


def BloombergCleaner(symbol):
    htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
  
    data=json.load(htmltext)
    datapoints=data["data_values"]
    cleaned=[]
    for data in datapoints:
        cleaned.append(data[1])
    return cleaned
    
def startingCleaner(symbol):
    htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
  
    data=json.load(htmltext)
    datapoints=data["prev_close"]
    return datapoints