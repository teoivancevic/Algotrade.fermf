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
secret = "2409877abc689bb3c40371f391000479"

'''
url = "http://192.168.1.101:3000"
api = ApiService(url)
secret = api.register(user)['secret']
print(secret)
'''

isFirstRun = True
tickLength = 3 # In seconds


class CalcTimeThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
 
    def run(self):
        self.value = calcStartTime()

'''
class TradingThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
 
    def run(self):
        self.value = calcStartTime()


class TickDelayThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
 
    def run(self):
        time.sleep(30)
'''

def printTickEnd():
    print(bcolors.OKCYAN + bcolors.BOLD + "Thread run done :)" + bcolors.ENDC)


try:

    timeThread = CalcTimeThread()
    timeThread.start()

    subprocess.run(["python3", "graphSabolicV2.py", user, secret]) # backup sabolicev

    timeThread.join()

    printTickEnd()

    while True:
        timeThread2 = CalcTimeThread()
        timeThread2.start()
        
        subprocess.run(["python3", "graphSabolicV2.py", user, secret]) # backup sabolicev
        
        isFirstRun = False
        

        #timeThread2.start()
        timeThread2.join()

        printTickEnd()
        

except:
    print("error")

#print(calcStartTime())