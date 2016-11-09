
import urllib
import re
import json
import time
import math

def DronesCleaner():
    htmltext=urllib.urlopen("http://api.dronestre.am/data")
    data=json.load(htmltext)
    alldata=[]
    for x in data["strike"]:
        if x["lat"] != "" and x["lon"]!= "":
            alldata.append([float((str(x["lat"]))),float((str(x["lon"])))])
        

    return alldata
def totalDrones():
    htmltext=urllib.urlopen("http://api.dronestre.am/data")
    data=json.load(htmltext)
    alldata={}
    counter=0
    for x in data["strike"]:
        alldata.setdefault("Total",0)
        alldata.setdefault("deaths",0)
        alldata.setdefault("injuries",0)
        alldata.setdefault("children",0)
        # x["deaths"]+=int((str(x['deaths_max'])))
        deathstring=(str(x['deaths_max']))
        alldata['Total'] +=1
        if deathstring.isdigit():
            int(deathstring)
            alldata["deaths"]+=int(deathstring)
        if str(x['injuries']).isdigit():
            int(str(x['injuries']))
            alldata["injuries"]+=int(str(x['injuries']))
        if str(x['children']).isdigit():
            int(str(x['children']))
            alldata["children"]+=int(str(x['children']))
    
    

    return alldata
    
