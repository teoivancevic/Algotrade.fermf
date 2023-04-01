import json
from ApiService import ApiService

url = "http://192.168.1.101:3000"
_api = ApiService(url)



secret = "1349d0f368babe13344db67d0c815bbb"
#print("from api: " + str(_api.getPairs("BTC,USD")))

print("form api: " + str(_api.getAllBalances(secret)))
