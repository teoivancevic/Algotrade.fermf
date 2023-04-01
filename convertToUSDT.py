from Services.InfoService import InfoService
from Services.bcolors import bcolors

user = "fermf_test1"
secret = "5a344c480cb7def87fc26aa1d276c84f"

info = InfoService()


print(bcolors.OKCYAN +  "USDT before: " + bcolors.BOLD +  str((info.getSpecificBalance(user, "USDT"))/(10**8)) + bcolors.ENDC)

response = info.allToUSDT(user, secret)
print(str(response))

print(bcolors.OKCYAN +  "USDT after: " + bcolors.BOLD +  str((info.getSpecificBalance(user, "USDT"))/(10**8)) + bcolors.ENDC)