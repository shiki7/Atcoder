from heapq import nlargest

x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = nlargest(k, (a + b for a in A for b in B))
ABC = nlargest(k, (ab + c for ab in AB for c in C))
[print(abc) for abc in ABC]
