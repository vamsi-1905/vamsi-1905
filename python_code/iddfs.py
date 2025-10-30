graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': [],
    '6': []
}

def dls(node, goal, limit, depth=0, path=None):
    if path is None:
        path = []

    path = path + [node]   # extend current path

    # Goal check
    if node == goal:
        return path

    # Stop if we hit depth limit
    if depth == limit:
        return None

    # Explore children
    for neigh in graph[node]:
        res = dls(neigh, goal, limit, depth+1, path)
        if res:
            return res
    return None

def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        print(f"Trying depth limit: {limit}")
        res = dls(start, goal, limit)
        if res:
            return res
    return None

# Example run
start = '1'
goal = '6'
max_depth = 3

path = iddfs(start, goal, max_depth)
if path:
    print("Path found:", path)
else:
    print("Goal not reachable within depth limit")
