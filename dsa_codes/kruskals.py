
#!/bin/python3

from math import math
import os


#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Create edge list as (weight, u, v)
    edges = []
    for u, v, w in zip(g_from, g_to, g_weight):
        # Order edge so u < v for tie-breaking
        edges.append((w, min(u, v), max(u, v)))

    # Sort edges:
    # 1. By weight
    # 2. By sum(u, v, w) for tie-breakers (could also just use (u, v))
    # 3. By lex order of u, v if still tied
    edges.sort(key=lambda x: (x[0], x[1] + x[2] + x[0], x[1], x[2]))

    # DSU data structure
    parent = [i for i in range(g_nodes + 1)]  # nodes are 1-indexed

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # Path compression
            u = parent[u]
        return u

    def union(u, v):
        parent[find(u)] = find(v)

    mst_weight = 0
    edge_count = 0

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_weight += w
            edge_count += 1
            if edge_count == g_nodes - 1:
                break
    return mst_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')

    fptr.close()
