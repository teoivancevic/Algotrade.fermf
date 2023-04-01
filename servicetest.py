from Services.ApiService import ApiService

api = ApiService("http://192.168.1.101:3000")

print(api.getTime())