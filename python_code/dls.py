
graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dls(graph,node,goal,max_depth,depth=0):

    if node==goal:
        print(node)
        return True

    if depth==max_depth:
        return False

    print("visiting",node)

    for neighbour in graph[node]:
        if dls(graph,neighbour,goal,max_depth,depth+1):
            return True

    return False

dls(graph,'5','8',2,0)






