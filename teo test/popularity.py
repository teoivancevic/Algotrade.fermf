from ApiService import ApiService
import json
from bcolors import bcolors

url = "http://192.168.1.101:3000"
_api = ApiService(url)

user = "fermf"
secret = "1349d0f368babe13344db67d0c815bbb"


allUsers = {"fermf", "zmaja90829"}

for user in allUsers:
    print(bcolors.OKCYAN + "User: " + user + bcolors.ENDC)
    balance = _api.balance(user)
    for line in balance:
        if(balance[line] !=0):
            print(line, balance[line])
    
    print("")
#
#balance = _api.balance("zmaja90829")

#for line in balance:
 #   if(balance[line] !=0):
  #      print(line, balance[line])
    
    #print(line)





