from ApiService import ApiService
api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()
graph = {}
node = []
vol_graph = {}
vol_mat = {}

def find(i, j):
    for k in range(len(graph[node[i]])):
        if graph[node[i]][k][0] == node[j]:
            return k
    return -1

def get_min_vol(i, j, k):
    return min(vol_mat[node[i]][node[j]], vol_mat[node[j]][node[k]], vol_mat[node[k]][node[i]]);


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
    node.append(key)
print(node.index('USDT'))

for i in range(5, 6):
    for j in range(len(node)):
        for k in range(len(node)):
            eij = find(i, j)
            ejk = find(j, k)
            eki = find(k, i)
            if eij != -1 and ejk != -1 and eki != -1:
                eij = graph[node[i]][eij][1] / 1e8
                ejk = graph[node[j]][ejk][1] / 1e8
                eki = graph[node[k]][eki][1] / 1e8
                if eij * ejk * eki > 1.001 and get_min_vol(i, j, k) > 0:
                    print('naso ciklus: ' + node[i] + ' ' + node[j] + ' ' + node[k] + ' omjer: ', eij * ejk * eki, 'vol: ', get_min_vol(i, j, k) / 1e8 )
                    trade_vol = get_min_vol(i, j, k) * 2 / 3


