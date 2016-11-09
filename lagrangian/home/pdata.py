import json
import urllib 
import time
import math 
import re
import random
from random import randint
symbolslist=['AAPL',]

def generateSymbolDaily():
    counter=0
    result=[]
    for symbol in symbolslist:
        htmltext= urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
        try:    
    	    data = json.load(htmltext)
    	    datapoints= data["data_values"]
        except ValueError:
            continue
        for point in datapoints:
            result.append("LVU"+str(point[0]%899809343))
    result = result*2
        
   
    return result

