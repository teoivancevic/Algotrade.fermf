from Services.ApiService import ApiService


class InfoService:

    def getSpecificBalance(self, user, crypto):
        api = ApiService("http://192.168.1.101:3000")
        balances = api.balance(user)
        return balances[crypto]

    def allToUSDT(self, user, secret):
        api = ApiService("http://192.168.1.101:3000")
        balances = api.balance(user)
        for line in balances:
            if(balances[line] !=0 and line != "USDT"):
                orderString =  line + "," + "USDT" + "," + str(balances[line])
                print(orderString)
                api.createOrders(user, secret, orderString)

