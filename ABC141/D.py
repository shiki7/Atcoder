import heapq

N, M = map(int, input().split())
a = list(map(int, input().split()))

q = []
for i in range(N):
    # 最も大きい値を取り出して1/2したいので、ここで反転させておき、最終的に足す時に戻す
    heapq.heappush(q, -a[i])
for i in range(M):
    l = heapq.heappop(q)
    heapq.heappush(q, -(-l//2))
print(-sum(q))
