from ApiService import ApiService
import time


api = ApiService("http://192.168.1.101:3000")

for i in range(100):
    print(api.getTime())
    time.sleep(0.15)