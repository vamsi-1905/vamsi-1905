graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(node, goal, depth, path):
    if depth == 0 and node == goal:
        return path + [node]
    if depth > 0:
        for nxt in graph[node]:
            res = dfs(nxt, goal, depth-1, path + [node])
            if res:
                return res
    return None

def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        print("Depth limit:", limit)
        ans = dfs(start, goal, limit, [])
        if ans:
            return ans
    return None


result = iddfs('A', 'F', 3)
print("Path found:", result if result else "No path")
