from threading import Thread
import urllib
import re
import json
import time
import math 
######


#####

def jsonToGeojsonol(url):
    htmltext= urllib.urlopen(url)
    # print htmltext
    data = json.load(htmltext)
    data= data["Data"]
    dumpeddata= json.dumps(data)
    print dumpeddata
# print jsonToGeojsonol("http://127.0.0.1:8000/media/traffic.json")


####################
def jsonToGeojson(url):
    
  
    htmltext= urllib.urlopen(url)
    data = json.load(htmltext)
    data= data["Data"]
    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "Point",
                "coordinates": [d["Longitude"], d["Latitude"]],
                },
            "properties" : d,
        } for d in data]
    }
    print geojson
print jsonToGeojson("http://127.0.0.1:8000/media/traffic.json")