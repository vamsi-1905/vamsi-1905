graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def dls(node, goal, graph, depth_limit, depth=0):
    if node == goal:
        print("Goal found:", node)
        return True

    if depth == depth_limit:
        return False

    print("Visiting:", node)

    for neighbour in graph[node]:
        if dls(neighbour, goal, graph, depth_limit, depth+1):
            return True

    return False

print("DLS traversal starting from node 5 (limit = 2):")
dls('5', '8', graph, 2)