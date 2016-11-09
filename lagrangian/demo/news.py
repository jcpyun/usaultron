import urllib
import re
import json
import time
import math

#https://newsapi.org/v1/articles?source=techcrunch&apiKey=8a284b7114cc49efa3f55b969b850f9a
def bloombergNews():
    apikey="8a284b7114cc49efa3f55b969b850f9a"
    htmltext=urllib.urlopen("https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey="+apikey)
    data=json.load(htmltext)
    if data['status']=="error":
        return {"Error":"Error"}
    output={}
    for x in xrange(len(data['articles'])):
        title=data['articles'][x]['title'] 
        url=data['articles'][x]['url'] 
        output.setdefault(title,"")
        output[title]=url
    return output

def bbcNews():
    apikey="8a284b7114cc49efa3f55b969b850f9a"
    htmltext=urllib.urlopen("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="+apikey)
    data=json.load(htmltext)
    if data['status']=="error":
        return {"Error":"Error"}
    output={}
    for x in xrange(len(data['articles'])):
        title=data['articles'][x]['title'] 
        url=data['articles'][x]['url'] 
        output.setdefault(title,"")
        output[title]=url
        
    return output
def othernews(source,sort):
    apikey="8a284b7114cc49efa3f55b969b850f9a"
    htmltext=urllib.urlopen("https://newsapi.org/v1/articles?source="+source+"&sortBy="+sort+"&apiKey="+apikey)
    data=json.load(htmltext)
    if data['status']=="error":
        return {"Error":"Error"}
    output={}
    for x in xrange(len(data['articles'])):
        title=data['articles'][x]['title'] 
        url=data['articles'][x]['url'] 
        output.setdefault(title,"")
        output[title]=url
    return output
    

def cleaner():
    symbols=["AAPL","EBAY","MSFT","TSLA","GOOGL","AMZN"]
    res={}
    for x in symbols:
        htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+x+":US")
        data=json.load(htmltext)
        datapoints=data["data_values"]
        datapoints=data["data_values"][len(datapoints)-1][1]
        res.setdefault(x,0)
        res[x]=datapoints
    return res
