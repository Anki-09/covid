import os
import requests
import json

def base(country):    
    data=""
    req=requests.get("https://api.covid19api.com/dayone/country/{}/status/confirmed".format(country))
    data=json.loads(req.text)
    return data
if __name__=="__main__":
    print(base("south-africa"))






















