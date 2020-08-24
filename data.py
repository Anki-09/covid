import os
import requests
import json

def base():    
    data=""
    req=requests.get("https://api.covid19api.com/countries")
    data=json.loads(req.text)
    return data
if __name__=="__main__":
    print(base())






















