# Graph as adjacency list
graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # using set for fast lookup

def dfs(graph, node):
    if node not in visited:
        print(node, end=" ")   # process node
        visited.add(node)      # mark as visited
        for neighbour in graph[node]:
            dfs(graph, neighbour)  # recursive call

# Driver code
print("DFS traversal starting from node 5:")
dfs(graph, '5')
