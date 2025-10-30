import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 6},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 3, 'G': 1},
    'G': {'D': 6, 'E': 2, 'F': 1}
}


def ucs(graph, start, goal):
    pq = []
    visited = set()
    heapq.heappush(pq, (0, [start]))

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for neigh, w in graph[node].items():
                if neigh not in visited:
                    heapq.heappush(pq, (cost + w, path + [neigh]))

    return None, None


start = 'A'
goal = 'G'
print(ucs(graph, start, goal))
