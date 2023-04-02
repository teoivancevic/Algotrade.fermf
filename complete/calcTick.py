import json
from Services.ApiService import ApiService
from datetime import datetime
import time
import sys

url = "http://192.168.1.101:3000"
_api = ApiService(url)

def calcTickTime(estimatedTime, curPrec, curTick, prec = 0.05, timeDelta = 3.):
    if (curPrec < prec): return estimatedTime
    curTime = time.time()
    time.sleep(estimatedTime - curPrec + timeDelta - curTime - 0.005)
    tickChanged = False
    tick = curTick
    tickdeltacalc = curPrec * 0.21
    while True:
        tick = _api.getTime()
        if (tick != curTick):
            return calcTickTime(time.time(), tickdeltacalc, prec, timeDelta)
        time.sleep(tickdeltacalc)

def bruteTime():
    curTick = _api.getTime()
    time.sleep(0.21)
    tick = curTick
    while True:
        tick = _api.getTime()
        if (tick != curTick):
            return time.time(), tick
        time.sleep(0.21)


def calcStartTime(tickLengthInSeconds):
    esttime, tick = bruteTime()
    #print(tickLengthInSeconds/(30*4), tickLengthInSeconds)
    return calcTickTime(esttime, 0.21, tick, max(0.05, tickLengthInSeconds/(30*4)), tickLengthInSeconds) # ZA TESTIRANJE, TICK 30
    #return calcTickTime(esttime, 0.21, tick, 0.05, 3)


if __name__ == "__main__":
    print(calcStartTime(30))


#print(datetime.fromtimestamp(calcTickTime(bruteTime(), 0.23, 0.005, 30)))
