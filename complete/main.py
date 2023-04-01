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


isFirstRun = True
tickLength = 30 # In seconds


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


#try:

timeThread = CalcTimeThread()
timeThread.start()

#subprocess.run(["python3", "graphSabolicV2.py"]) # backup sabolicev

generateAllPairsJsonFile() # ToDo zamijenit s boljim nacinom
url = "http://192.168.1.101:3000"
api = ApiService(url)

pairsJson = api.getAllPairs()
#print(pairsJson)
print("a")
prettyJson = json.dumps(pairsJson, indent=4) # ovo je tocno
#print(prettyJson)

program_path = "./bellman"

cppFile = Popen([program_path], stdout=PIPE, stdin=PIPE)
cppFile.comm
cppFile.stdin.write(bytes(prettyJson, "utf-8"))
cppFile.stdin.flush()

'''
for line in prettyJson:
    cppFile.stdin.write(bytes(line + '\n', "utf-8"))
'''
print("bbb")

trades = cppFile.stdout.readline().strip().decode("utf-8")#.strip().split("|")
print("All trades: " + trades)
#pritn(trades)
#print("test 3")
for trade in trades:

    print("Trade: " + trade)

print("test 4")





timeThread.join()

printTickEnd()

while True:
    timeThread2 = CalcTimeThread()
    timeThread2.start()
    
    #subprocess.run(["python3", "graphSabolicV2.py"]) # backup sabolicev
    



    
    isFirstRun = False
    

    #timeThread2.start()
    timeThread2.join()

    printTickEnd()
    

#except:
print("error")

#print(calcStartTime())