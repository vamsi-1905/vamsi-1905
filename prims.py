#!/bin/python3

from math import math
import os
import heapq

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    graph={i:[]for i in range(1,n+1)}
    for u,v,w in edges:
        graph[u].append((w,v))
        graph[v].append((w,u))

        visited=set()
        min_heap=[]

        visited.add(start)
        for w,v in graph[start]:
            heapq.heappush(min_heap,(w,v))

        total_weight=0

        while min_heap and len(visited)<n:
            w,v = heapq.heappop(min_heap)
            visited.add(v)
            total_weight+=w
            for next_w,next_v in graph[v]:
                if next_w not in visited:
                    heapq.heappush(min_heap,(next_v,next_w))





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
