import sys

from Services.ApiService import ApiService
from Services.bcolors import bcolors

api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()
graph = {}
node = []
vol_graph = {}
vol_mat = {}
e_mat = {}

user = sys.argv[1]
secret = sys.argv[2]


def find(i, j):
    for k in range(len(graph[node[i]])):
        if graph[node[i]][k][0] == node[j]:
            return k
    return -1

def get_min_vol(i, j, k, eij, ejk, eki):
    first = vol_mat[node[i]][node[j]] 
    second = min(first * eij, vol_mat[node[j]][node[k]])
    third = min(second * ejk, vol_mat[node[k]][node[i]])
    return int(min(first, second / ejk, third / eki / ejk))


print('bal na pocetku: ', api.balance(user)['USDT'] / 1e8)

for key in data:
    if key.startswith('close') == True:
        node1 = key.split('_')[1].split(',')[0]
        node2 = key.split('_')[1].split(',')[1]

        if not (node1 in graph):
            graph[node1] = []
        graph[node1].append((node2, data[key]))

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
    e_mat[key] = {}
    for x in graph[key]:
        e_mat[key][x[0]] = x[1]

for key in graph:
    node.append(key)
print(node.index('USDT'))

for i in range(3, 4):
    for j in range(len(node)):
        for k in range(len(node)):
            if j == k:
                continue

            if node[j] in e_mat[node[i]] and node[k] in e_mat[node[j]] and node[i] in e_mat[node[k]]:
                #eij = graph[node[i]][eij][1] / 1e8
                #ejk = graph[node[j]][ejk][1] / 1e8
                #eki = graph[node[k]][eki][1] / 1e8
                eij = e_mat[node[i]][node[j]] / 1e8
                ejk = e_mat[node[j]][node[k]] / 1e8
                eki = e_mat[node[k]][node[i]] / 1e8

                if eij * ejk * eki > 1.001 and get_min_vol(i, j, k, eij, ejk, eki) / 1e8 > 0.002:
                    print("uso")
                    #print('naso ciklus: ' + node[i] + ' ' + node[j] + ' ' + node[k] + ' omjer: ', eij * ejk * eki, 'vol: ', get_min_vol(i, j, k, eij, ejk, eki) / 1e8 )

                    #if get_min_vol(i, j, k, eij, ejk, eki) / 1e8 > 20:
                    print(node[i], '->', node[j], eij, vol_mat[node[i]][node[j]] / 1e8)
                    print(node[j], '->', node[k], ejk, vol_mat[node[j]][node[k]] / 1e8)
                    print(node[k], '->', node[i], eki, vol_mat[node[k]][node[i]] / 1e8)

                    trade_vol = min(int(get_min_vol(i, j, k, eij, ejk, eki) / eij * 9 / 10), int(int(api.balance(user)['USDT']) * 9 / 10))
                    print('vol: ', trade_vol / 1e8)

                    trade_vol = int(trade_vol)
                    #print('bal: ', api.balance(user)['USDT'] / 1e8, 'est_new_bal: ', trade_vol / 1e8 * eij * ejk * eki) 
                    #print('trade_vol_nacpo[cetaku', trade_vol, vol_mat[node[i]][node[j]])

                    url = node[i] + ',' + node[j] + ',' + str(trade_vol)
                    trade_vol = int(trade_vol * eij)
                    #print('trade_vol_drugitrade', trade_vol)

                    url = url + '|' + node[j] + ',' + node[k] + ',' + str(trade_vol)
                    trade_vol = int(trade_vol * ejk)
                    url = url + '|' + node[k] + ',' + node[i] + ',' + str(trade_vol)
                    print(url)
                    print(api.createOrders(user, secret, url))
                    print('bal: ', api.balance(user)['USDT'] / 1e8)
                    print('------')
                    #exit(0)



print(bcolors.OKGREEN + str(api.balance(user)['USDT'] / 1e8) + bcolors.ENDC)
