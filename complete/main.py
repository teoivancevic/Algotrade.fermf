from calcTick import calcStartTime
#import graphSabolic


import subprocess
from threading import Thread
from Services.bcolors import bcolors
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


try:

    timeThread = CalcTimeThread()
    timeThread.start()
    subprocess.run(["python3", "graphSabolic.py"])

    
    timeThread.join()

    printTickEnd()

    while True:
        timeThread2 = CalcTimeThread()
        timeThread2.start()
        subprocess.run(["python3", "graphSabolic.py"])
        
        isFirstRun = False
        

        #timeThread2.start()
        timeThread2.join()

        printTickEnd()
        

except:
    print("error")

#print(calcStartTime())