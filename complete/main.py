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
        if(isFirstRun):
            self.value = calcStartTime()
        else:
            time.sleep(tickLength)

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


try:


    while True:
        if(isFirstRun):
            timeThread = CalcTimeThread()#Thread(target = calcStartTime())
            #tradingThread = TradingThread()
            subprocess.run(["python3", "graphSabolic.py"])


            #starts threads
            #tradingThread.start()
            timeThread.start()

            # waits for thread end
            #tradingThread.join()
            timeThread.join()
            subprocess.run(["python3", "graphSabolic.py"])

            #data = timeThread.value
            #print(data)

            isFirstRun = False

        else:
            print("inside else block")
            #timeThread2 = TickDelayThread()
            timeThread2 = CalcTimeThread()
            subprocess.run(["python3", "graphSabolic.py"])

            #tradingThread = TradingThread()


            #tradingThread.start()
            timeThread2.start()


            #tradingThread.join()
            timeThread2.join()
            subprocess.run(["python3", "graphSabolic.py"])

        print(bcolors.OKCYAN + bcolors.BOLD + "Thread run done :)" + bcolors.ENDC)

except:
    print("error")

#print(calcStartTime())