graph ={
'1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': [],
    '6': []
}
queue=[]
visited=[]

def dfs(graph,visited,start):
    queue.append(start)
    visited.append(start)

    while queue:
        m=queue.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

dfs(graph,visited,'1')
