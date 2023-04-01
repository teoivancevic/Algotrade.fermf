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
    balancesreq = _api.balance(user)
    balances = balancesreq
    print(balances["USDT"])
    while True: 
        time.sleep(1/19);
        nbalancesreq = _api.balance(user)
        nbalances = nbalancesreq
        print(nbalances["USDT"])
        if (nbalances["USDT"] != balances["USDT"]):
            with open(f"{user}.balances1.txt", "w") as f:
                f.write(balancesreq.text)
            with open(f"{user}.balances2.txt", "w") as f:
                f.write(nbalancesreq.text)


getBal("stackforces")
