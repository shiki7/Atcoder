import heapq

n, k = map(int, input().split())
h = list(map(int, input().split()))

heapq.heapify(h)
if n-k >= 0:
    print(sum(heapq.nsmallest(n-k, h)))
else:
    print(0)
