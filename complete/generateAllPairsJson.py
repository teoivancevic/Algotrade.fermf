from Services.ApiService import ApiService
import json

def generateAllPairsJsonFile():
    url = "http://192.168.1.101:3000"
    api = ApiService(url)

    response = api.getAllPairs()

    with open("allPairs.json", "w") as outfile:
        json.dump(response, outfile, ensure_ascii=False, indent=4)

    #print("Done")

