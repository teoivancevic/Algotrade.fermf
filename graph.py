import sys
import random

sys.path.append('teo_test/')

from ApiService import ApiService
api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()
graph = {}
node = []
vol_graph = {}
vol_mat = {}
e_mat = {}
user='fermf'
secret='1349d0f368babe13344db67d0c815bbb'


def find(i, j):
    for k in range(len(graph[node[i]])):
        if graph[node[i]][k][0] == node[j]:
            return k
    return -1

def get_path_vol(path):
    vals = []
    vals.append(vol_mat[node[path[0]]][node[path[1]]])
    for i in range(1, len(path) - 1):
        vals.append(min(vals[-1] * (e_mat[node[path[i]]][node[path[i + 1]]] / 1e8), vol_mat[node[path[i]]][node[path[i + 1]]]))

    ret = vals[0]
    div = 1
    for i in range(1, len(vals)):
        div *= e_mat[node[path[i]]][node[path[i + 1]]] / 1e8
        #print('vals[' + str(i) + ']', vals[i])
        ret = min(ret, vals[i] / div)
        #print('div', div)
    return int(ret)

def get_min_vol(i, j, k, eij, ejk, eki):
    first = vol_mat[node[i]][node[j]] 
    second = min(first * eij, vol_mat[node[j]][node[k]])
    third = min(second * ejk, vol_mat[node[k]][node[i]])
    print('get_min_vol', first, second, third, eki * ejk)
    return int(min(first, second / ejk, third / eki / ejk))


print('bal na pocetku: ', api.balance(user)['USDT'] / 1e8)

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
        vol_graph[node1].append((node2, data[key]));


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

def find_trig(i):
    for j in range(len(node)):
        for k in range(len(node)):
            if j == k:
                continue



def order_path(path):
    trade_vol = min(int(get_path_vol(path) / (e_mat[node[path[0]]][node[path[1]]] / 1e8) * 9 / 10), int(int(api.balance(user['USDT']) * 9 /10)))
    trade_vol = int(trade_vol)

    print('vol: ', trade_vol / 1e8)
    print('bal: ', api.balance(user)['USDT'] / 1e8, 'est_new_bal: ', trade_vol / 1e8 * eij * ejk * eki) 
    url = ""
    for i in range(len(path) - 1):
        url += node[path[i]] + ',' + node[path[i + 1]] + str(trade_vol) + '|'
        trade_vol = int(trade_vol * (e_mat[node[path[i]]][node[path[i + 1]]] / 1e8))

    url = url[:-1]
    print(url)
    print(api.createOrders(user, secret, url))
    print('bal: ', api.balance(user)['USDT'] / 1e8)
    print('------')






            if node[j] in e_mat[node[i]] and node[k] in e_mat[node[j]] and node[i] in e_mat[node[k]]:
                eij = e_mat[node[i]][node[j]] / 1e8
                ejk = e_mat[node[j]][node[k]] / 1e8
                eki = e_mat[node[k]][node[i]] / 1e8
                #print(eij* ejk* eki)

                #print('vol_paths: ', get_path_vol([i, j, k, i]) / 1e8, get_min_vol(i, j, k, eij, ejk, eki) / 1e8)
                if eij * ejk * eki > 1.001 and get_path_vol([i, j, k, i]) / 1e8 > 0.002:
                    print("uso")

                    #if get_min_vol(i, j, k, eij, ejk, eki) / 1e8 > 20:
                    print(node[i], '->', node[j], eij, vol_mat[node[i]][node[j]] / 1e8)
                    print(node[j], '->', node[k], ejk, vol_mat[node[j]][node[k]] / 1e8)
                    print(node[k], '->', node[i], eki, vol_mat[node[k]][node[i]] / 1e8)

                    trade_vol = min(int(get_path_vol([i, j, k, i]) / eij * 9 / 10), int(int(api.balance(user)['USDT']) * 9 / 10))
                    print('vol: ', trade_vol / 1e8)

                    trade_vol = int(trade_vol)
                    print('bal: ', api.balance(user)['USDT'] / 1e8, 'est_new_bal: ', trade_vol / 1e8 * eij * ejk * eki) 

                    url = node[i] + ',' + node[j] + ',' + str(trade_vol)
                    trade_vol = int(trade_vol * eij)

                    url = url + '|' + node[j] + ',' + node[k] + ',' + str(trade_vol)
                    trade_vol = int(trade_vol * ejk)
                    url = url + '|' + node[k] + ',' + node[i] + ',' + str(trade_vol)
                    print(url)
                    print(api.createOrders(user, secret, url))
                    print('bal: ', api.balance(user)['USDT'] / 1e8)
                    print('------')



def cmp(a):
    return a[1]

HOP_DIST=1
CURR_NODE=5
path = [5]
for az in range(HOP_DIST):
    vols = []
    for neigh in vol_graph[node[CURR_NODE]]:
        neigh_idx = node.index(neigh[0])
        vols.append((neigh_idx, min(neigh[1] / e_mat[node[CURR_NODE]][node[neigh_idx]], vol_mat[node[neigh_idx]][node[CURR_NODE]])))

    vols.sort(reverse=True,key=cmp)
    next_node = min(len(vols), random.randint(0, 5))
    path.append(next_node)
    CURR_NODE = next_node


find_trig(5)

print(api.balance(user)['USDT'] / 1e8)
