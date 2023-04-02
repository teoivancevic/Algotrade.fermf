import sys

sys.path.append('teo test/')

from ApiService import ApiService
api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()

with open("teo test/allPairs.json", "w") as f:
    f.write(str(data));

