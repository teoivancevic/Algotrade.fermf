from Services.ApiService import ApiService


class InfoService:
    def __init__(self, base_url):
        self.url = base_url

    def getSpecificBalance(self, user, crypto):
        api = ApiService(self.url)
        balances = api.balance(user)
        return balances[crypto]

    def allToUSDT(self, user, secret):
        api = ApiService(self.url)
        balances = api.balance(user)
        for line in balances:
            if(balances[line] !=0 and line != "USDT"):
                orderString =  line + "," + "USDT" + "," + str(balances[line])
                print(orderString)
                response = api.createOrders(user, secret, orderString)
                return response

