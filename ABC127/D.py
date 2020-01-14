import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
bc = [list(map(int, input().split())) for _ in range(m)]
bc = sorted(bc, key=lambda x: -x[1])
for b, c in bc:
    for _ in range(b):
        x = heapq.heappop(a)
        if c > x:
            heapq.heappush(a, c)
        else:
            heapq.heappush(a, x)
            break
print(sum(a))
