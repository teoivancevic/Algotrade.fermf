from calcTick import calcStartTime
#import graphSabolic
from generateAllPairsJson import generateAllPairsJsonFile

import json

import subprocess
from subprocess import Popen, PIPE

from threading import Thread
from Services.bcolors import bcolors
from Services.ApiService import ApiService
from Services.InfoService import InfoService
import time



user = "fermf"
secret = "bf32102aa7c09e2d13feae217db7dff2"

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

#generateAllPairsJsonFile() # ToDo zamijenit s boljim nacinom
url = "http://192.168.1.101:3000"
api = ApiService(url)
info = InfoService(url)

print("Begin USDT: " + str(info.getSpecificBalance(user, "USDT")))


# Vito file start
pairsJson = api.getAllPairs()

prettyJson = json.dumps(pairsJson, indent=4) # ovo je tocno

program_path = "./bellman"

cppFile = Popen([program_path], stdout=PIPE, stdin=PIPE)

cppFile.communicate(bytes(prettyJson, "utf-8"))

trades = str(cppFile.communicate()[0]).split('\'')[1][:-2]
#trades = trades.split('|')

#pritn(trades)
#print("test 3")

response = api.createOrders(user, secret, trades)
print("Trades: " + trades)
print(trades + str(response))

'''
for trade in trades:
    response = api.createOrders(user, secret, trade)
    print("Trade: " + trade)
    print(str(response))
    print()
    '''
# Vito file end

print(bcolors.OKGREEN + bcolors.BOLD + str(info.getSpecificBalance(user, "USDT") / 1e8) + bcolors.ENDC)



timeThread.join()

printTickEnd()

while True:
    timeThread2 = CalcTimeThread()
    timeThread2.start()
    
    #subprocess.run(["python3", "graphSabolicV2.py"]) # backup sabolicev
    
    # Vito file start
    pairsJson = api.getAllPairs()

    prettyJson = json.dumps(pairsJson, indent=4) # ovo je tocno

    program_path = "./bellman"

    cppFile = Popen([program_path], stdout=PIPE, stdin=PIPE)

    cppFile.communicate(bytes(prettyJson, "utf-8"))

    trades = str(cppFile.communicate()[0]).split('\'')[1][:-2]
    #trades = trades.split('|')

    #pritn(trades)
    #print("test 3")

    response = api.createOrders(user, secret, trades)
    print("Trades: " + trades)
    print(str(response))
    '''
    for trade in trades:
        response = api.createOrders(user, secret, trade)
        print("Trade: " + trade)
        print(str(response))
        print()
        '''
    # Vito file end

    print(bcolors.OKGREEN + bcolors.BOLD + str(info.getSpecificBalance(user, "USDT") / 1e8) + bcolors.ENDC)


    
    isFirstRun = False
    

    #timeThread2.start()
    timeThread2.join()

    printTickEnd()
    

#except:
print("error")

#print(calcStartTime())