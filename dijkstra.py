def dijkstra(n, edges, start):
    graph = {str(i): [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist = {str(i): float('inf') for i in range(n)}
    dist[start] = 0
    visited = set()

    while len(visited) < n:
        min_node = None
        for node in dist:
            if node not in visited and (min_node is None or dist[node] < dist[min_node]):
                min_node = node
        visited.add(min_node)
        for neighbor, weight in graph[min_node]:
            if dist[min_node] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_node] + weight

    return dist
