from Services.ApiService import ApiService
from Services.InfoService import InfoService
from Services.bcolors import bcolors
api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()
graph = {}
node = []
vol_graph = {}
vol_mat = {}


user = "fermf_test1"
secret = "5a344c480cb7def87fc26aa1d276c84f"

info = InfoService()
#print(info.getSpecificBalance(user, "USDT"))
startUSDT = info.getSpecificBalance(user, "USDT")
print(bcolors.OKCYAN + "Balance before: " + str(startUSDT) + bcolors.ENDC)



def find(i, j):
    for k in range(len(graph[node[i]])):
        if graph[node[i]][k][0] == node[j]:
            return k
    return -1


for key in data:
    if key.startswith('close') == True:
        node1 = key.split('_')[1].split(',')[0]
        node2 = key.split('_')[1].split(',')[1]

        if not (node1 in graph):
            graph[node1] = []
        graph[node1].append((node2, data[key]));

    if key.startswith('vol') == True:
        node1 = key.split('_')[1].split(',')[0]
        node2 = key.split('_')[1].split(',')[1]

        if not (node1 in vol_graph):
            vol_graph[node1] = []
        vol_graph[node1].append((node2, data[key]))


for key in vol_graph:
    vol_mat[key] = {}
    for x in vol_graph[key]:
        vol_mat[key][x[0]] = x[1]

for key in graph:
    node.append(key)
print(node.index('USDT'))

for i in range(5, 6):
    for j in range(len(node)):
        for k in range(len(node)):
            eij = find(i, j)
            ejk = find(j, k)
            eki = find(k, i)
            if eij != -1 and ejk != -1 and eki != -1:
                eij = graph[node[i]][eij][1] / (10**8)
                ejk = graph[node[j]][ejk][1] / (10**8)
                eki = graph[node[k]][eki][1] / (10**8)
                if eij * ejk * eki > 1.001:
                    # found positive cycle
                    min_vol = min(vol_mat[node[i]][node[j]], vol_mat[node[j]][node[k]], vol_mat[node[k]][node[i]])
                    print('naso ciklus: ' + node[i] + ' ' + node[j] + ' ' + node[k] + ' omjer: ', eij * ejk * eki, 'vol: ', min_vol)
                    
                    if(min_vol != 0):
                        vol1 = 100 * (10**8)
                        orderString1 = node[i] + "," + node[j] + "," + str(vol1)
                        api.createOrders(user, secret, orderString1)

                        vol2 = info.getSpecificBalance(user, node[j])
                        #if(vol2 > 0):
                        orderString2 = node[j] + "," + node[k] + "," + str(vol2)
                        api.createOrders(user, secret, orderString2)
                            
                        vol3 = info.getSpecificBalance(user, node[k])
                        #    if(vol3 > 0):
                        orderString3 = node[k] + "," + node[i] + "," + str(vol3)

                        currUSDT = info.getSpecificBalance(user, "USDT")
                        print("Current USDT: " + str(currUSDT))
                    
                    

endUSDT = info.getSpecificBalance(user, "USDT")
print(bcolors.OKCYAN + "Balance after: " + bcolors.BOLD + str(endUSDT) + bcolors.ENDC)
print()
print("Difference USDT: " + str((endUSDT - startUSDT)/(10**8)))



