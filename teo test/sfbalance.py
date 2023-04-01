import json
from ApiService import ApiService
from datetime import datetime
import time

url = "http://192.168.1.101:3000"
_api = ApiService(url)


user = "fermf"
secret = "1349d0f368babe13344db67d0c815bbb"
#print("from api: " + str(_api.getPairs("BTC,USD")))


def getBal(user):
    balances = json.loads(_api.balance(user))
    
    while True:
        
        time.sleep(1/21);



