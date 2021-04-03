import sys
sys.setrecursionlimit(2000)

m, n = map(int, input().split())


def calc(m, n):
    if m == 0:
        return n+1
    elif m == 1:
        return n+2
    elif m == 2:
        return 2*n+3
    else:
        return 2**(n+3)-3


print(calc(m, n))
