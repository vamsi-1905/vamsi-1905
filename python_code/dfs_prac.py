graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited=set()

def dfs(graph,visited,node):
    if node not in visited:
        visited.add(node)
        print(node)

        for neighbour in graph[node]:
            dfs(graph,visited,neighbour)

dfs(graph,visited,'5')