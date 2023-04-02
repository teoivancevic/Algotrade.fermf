from calcTick import calcStartTime
#import graphSabolic
from generateAllPairsJson import generateAllPairsJsonFile

import json

import subprocess
from subprocess import Popen, PIPE

from threading import Thread
from Services.bcolors import bcolors
from Services.ApiService import ApiService
import time


user = "fermf"
secret = "c0d93a7a531b7d89b6d3a6ccbc3754d3"

concurrentTradingThreads = 10

url = "http://192.168.1.101:3000"
api = ApiService(url)
#secret = api.register(user)['secret']
#print(secret)

data = api.getAllPairs()


isFirstRun = True
tickLength = 30 # In seconds


class CalcTimeThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
 
    def run(self):
        if isFirstRun:
            self.value = calcStartTime(tickLength)
        else:
            time.sleep(tickLength)


class FileThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        subprocess.run(["python3", "graphSabolicV5.py", user, secret, json.dumps(data).replace(" ", "")])


def printTickEnd():
    print(bcolors.OKCYAN + bcolors.BOLD + "Thread run done :)" + bcolors.ENDC)


#try:

resp = api.resetBalance(user, secret)
print(resp)

timeThread = CalcTimeThread()
timeThread.start()

threads = []
for i in range(concurrentTradingThreads):
    thread = FileThread()
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(bcolors.OKBLUE + str(api.balance(user)["USDT"] / 1e8) + bcolors.ENDC)


#subprocess.run(["python3", "graphSabolicV2.py", user, secret]) # backup sabolicev

timeThread.join()

printTickEnd()

while True:
    timeThread2 = CalcTimeThread()
    timeThread2.start()
    data = api.getAllPairs()
    
    #subprocess.run(["python3", "graphSabolicV2.py", user, secret]) # backup sabolicev

    threads = []
    for i in range(concurrentTradingThreads):
        thread = FileThread()
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print(bcolors.OKBLUE + str(api.balance(user)["USDT"] / 1e8) + bcolors.ENDC)


    
    isFirstRun = False
    

    #timeThread2.start()
    timeThread2.join()

    printTickEnd()
    

#except:
print("error")

#print(calcStartTime())