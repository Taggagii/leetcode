####def findRedundantConnection(edges):
####    n = len(edges)
####
####    save_edges = edges.copy()
####    edges = [[min(i), max(i)] for i in edges]
####    structure = {i : [] for i in range(1, n + 1)}
####    
####    for i in edges:
####        structure[i[0]].append(i[1])
####        structure[i[1]].append(i[0])
####    for i in structure:
####        print(i, structure[i])
####    non_redundant = [i for i in structure.keys() if len(structure[i]) == 1]
####    
####    for i in structure:
####        structure[i] = [x for x in structure[i] if x not in non_redundant]
####        
####    non_redundant += [i for i in structure.keys() if len(structure[i]) == 1]
####    
####    for i in non_redundant:
####        structure[i] = []
####    
####    for i in range(n - 1, -1, -1):
####        if save_edges[i][1] in structure[save_edges[i][0]]:
####            return save_edges[i]
####    return 0
    
def findRedundantConnection(edges):
    n = len(edges)

    save_edges = edges.copy()
    edges = [[min(i), max(i)] for i in edges]
    structure = {i : [] for i in range(1, n + 1)}
    
    for i in edges:
        structure[i[0]].append(i[1])
        structure[i[1]].append(i[0])
        
    useless = [i for i in structure if len(structure[i]) == 1]
    while useless != []:
        for i in useless:
            structure[i] = []
        for i in structure:
            structure[i] = [x for x in structure[i] if x not in useless]
            
        useless = [i for i in structure if len(structure[i]) == 1]

    
    for i in range(n - 1, -1, -1):
            if save_edges[i][1] in structure[save_edges[i][0]]:
                return save_edges[i]
    return 0

import time
s = time.time()
print(findRedundantConnection([[1,2],[1,3],[2,3]]) == [2, 3])

print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1, 4])

print(findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]) == [3, 5])

print(findRedundantConnection([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]) == [4, 10])

print(findRedundantConnection([[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]) == [1, 4])
print(10000 * (time.time() - s))
