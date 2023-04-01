import json
from Services.ApiService import ApiService
from datetime import datetime
import time

url = "http://192.168.1.101:3000"
_api = ApiService(url)


def calcTickTime(estimatedTime, curPrec, curTick, prec = 0.05, timeDelta = 3.):
    if (curPrec < prec): return estimatedTime
    curTime = time.time()
    time.sleep(estimatedTime - curPrec + timeDelta - curTime - 0.005)
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
        if (tick != curTick):
            return time.time(), tick
        time.sleep(0.22)


def calcStartTime():
    esttime, tick = bruteTime()
    return calcTickTime(esttime, 0.22, tick, 0.25, 30)


if __name__ == "__main__":
    print(calcStartTime())


#print(datetime.fromtimestamp(calcTickTime(bruteTime(), 0.23, 0.005, 30)))
