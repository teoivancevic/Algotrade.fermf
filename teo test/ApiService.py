import requests


class ApiService:

    def __init__(self, base_url):
        self.url = base_url

    def getPairs(self, pairs):
        response = requests.get(self.url + "/getPairs/" + pairs)
        return response.json()

    def getTime(self):
        response = requests.get(self.url + "/getTime")
        while(response.status_code == 429):
            response = requests.get(self.url + "/getTime")
        
        return response.json()


        
        

    def getAllPairs(self):
        response = requests.get(self.url + "/getAllPairs")
        return response.json()
    
    def getHistorisalPairs(self, time_to_get, pairs):
        response = requests.get(self.url + "/getHistoricalPairs/" + time_to_get + "/" + pairs)
        return response.json()
    
    def createOrders(self, user, secret, orders):
        response = requests.post(self.url + "/createOrders/" + user + "/" + secret + "/" + orders)
        return response.json()

    def register(self, user):
        response = requests.post(self.url + "/register/" + user)
        return response.json()

    def resetBalance(self, user, secret):
        response = requests.post(self.url + "/resetBalance/" + user + "/" + secret)
        return response.json()
    
    def balance(self, user):
        response = requests.get(self.url + "/balance/" + user)
        return response.json()

    def index(self):
        response = requests.get(self.url + "/")
        return response.json()

    def getAllBalances(self, secret):
        response = requests.get(self.url + "/getAllBalances" + "?secret=" + secret)
        return response.json()

    def getAllBalancesCondensed(self, secret):
        response = requests.get(self.url + "/getAllBalancesCondensed" + "?secret=" + secret)
        return response.json()

    def getIPsAndWrongRequests(self, secret):
        response = requests.get(self.url + "/getIPsAndWrongRequests" + "?secret=" + secret)
        return response.json()    
