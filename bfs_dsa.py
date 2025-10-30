#!/bin/python3

from math import math
import os


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    graph = {i:[] for i in range(1,n+1)}
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1]*(n+1)
    dist[s]=0
    q = deque([s])

    while q:
        node = q.popleft()
        for neighbour in graph[node]:
            if dist[neighbour]==-1:
                dist[neighbour]=dist[node]+6
                q.append(neighbour)


    result=[]
    for i in range(1,n+1):
        if i!=s:
            result.append(dist[i])

    return result


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
