#!/bin/python3

from math import math

if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

    if m <= (n-1)*(n-2)//2+1:
        print(m+s-(n-1))
    else:
        s -=n-1
        e = m - (n-1)*(n-2)//2
        mnc = s + (n-2)//(n-1)
        ans = 1e42
        s-=mnc

        for A in [0,s//(n-2),s//(n-2)+1]:
            for B in [0,n-3,(s-A*(n-2)//(n-1))]:
                x = A*(n-2)+B
                ans = min(ans,(s-x+mnc)*e+(n-1)*(n-2)//2*A+B*(B-1)//2+B*(n-B-1))

    print(ans+m)