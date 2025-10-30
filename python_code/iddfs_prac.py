graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': [],
    '6': []
}

def dls(graph,start,goal,depth,limit,path=None):

    if path is None:
        path=[]

    path = path+[start]

    if start==goal:
        return path

    if depth==limit:
        return None

    for neigh in graph[start]:
        res = dls(graph,start,goal,depth+1,limit,path)
        if res:
            return res
    return None

def iddfs(graph,start,goal,max_depth):
    for limit in range(max_depth+1):
        print("trying limit",limit)
        res = dls(graph,start,goal,0,limit)
        if res:
            return res
    return None

start = '1'
goal = '6'
max_depth = 3

path = iddfs(graph,start, goal, max_depth)
if path:
    print("Path found:", path)
else:
    print("Goal not reachable within depth limit")





