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

tickChanged = False
countChanges = 0
tick = _api.getTime()
lastTick = tick

timeChanged = datetime.now()
lastTime = datetime.now()

while countChanges < 5:
    tick = _api.getTime()
    if(tick != lastTick):
        #tickChanged = True
        timeChanged = datetime.now()
        countChanges += 1
        print(str(lastTime), str(timeChanged), str(tick))
        #break
    #else:
        #print(str(datetime.now()) + ": " + str(tick))  

    time.sleep(0.25)

    lastTick = tick
    lastTime = datetime.now()

#print("Tick changed to " + str(tick) + " at " + str(timeChanged))
#print(str(lastTime), str(timeChanged), str(tick))
