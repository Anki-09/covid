import os
import requests
import json

def base(country):    
    data=""
    req=requests.get("https://api.covid19api.com/dayone/country/{}/status/confirmed".format(country))
    data=json.loads(req.text)
    return data
def get_total():
    url="https://api.covid19api.com/total/dayone/country/south-africa/status/confirmed"
    data={}
    req=requests.get(url)
    if req.status_code==200:
        data=json.loads(req.text)
    return data
if __name__=="__main__":
    print(base("canada"))
    print(get_total())























