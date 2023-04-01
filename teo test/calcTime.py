import json
from ApiService import ApiService
from datetime import datetime
import time

url = "http://192.168.1.101:3000"
_api = ApiService(url)


user = "fermf"
secret = "1349d0f368babe13344db67d0c815bbb"
#print("from api: " + str(_api.getPairs("BTC,USD")))

balances = _api.balance(user)
#print("Balance: " + str(_api.balance(user)))

#print("form api: " + str(_api.getAllBalances(secret)))

def calcTickTime(estimatedTime, curPrec, curTick, prec = 0.05, timeDelta = 3.):
    if (curPrec < prec): return estimatedTime
    curTime = time.time()
    time.sleep(estimatedTime - curPrec + timeDelta - curTime - 0.0001)
    tickChanged = False
    tick = curTick
    tickdeltacalc = curPrec * 0.22
    while True:
        tick = _api.getTime()
        if (tick != curTick):
            return calcTickTime(time.time(), tickdeltacalc, prec, timeDelta)
        time.sleep(tickdeltacalc)

def bruteTime():
    curTick = _api.getTime()
    time.sleep(0.22)
    tick = curTick
    while True:
        tick = _api.getTime()
        print(time.time(), tick, curTick)
        if (tick != curTick):
            return time.time(), tick
        time.sleep(0.22)

estTime, tick = bruteTime()
print(calcTickTime(estTime, 0.22, tick, 0.05, 30))


#print(datetime.fromtimestamp(calcTickTime(bruteTime(), 0.23, 0.005, 30)))

