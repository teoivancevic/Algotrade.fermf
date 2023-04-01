from ApiService import ApiService
api = ApiService('http://192.168.1.101:3000')

data = api.getAllPairs()
graph = {}

for key in data:
    if key.startswith('close') == True:
        node1 = key.split('_')[1].split(',')[0]
        node2 = key.split('_')[1].split(',')[1]

        if not (node1 in graph):
            graph[node1] = []
        graph[node1].append((node2, data[key]));


node = []
for key in graph:
    node.append(key)

for i in range(len(node)):
    for j in range(len(node)):
        for k in range(len(node)):
            eij = graph[node[i]].find(j)
            ejk = graph[node[j]].find(k)
            eki = graph[node[k]].find(i)
            if eij != -1 and ejk != -1 and eki != -1:
                eij = graph[node[i]][eij] / 1e8
                ejk = graph[node[j]][ejk] / 1e8
                eki = graph[node[k]][eki] / 1e8
                if eij * ejk * eki > 1:
                    print('naso ciklus: ' + node[i] + ' ' + node[j] + ' ' + node[k])


