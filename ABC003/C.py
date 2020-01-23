import heapq

n, k = map(int, input().split())
r = list(map(int, input().split()))
r = list(map(lambda x: x*(-1), r))

heapq.heapify(r)
ans = 0
watch_list = []
for _ in range(k):
    watch_list.append(heapq.heappop(r)*(-1))
for w in reversed(watch_list):
    ans = (ans + w) / 2
print(ans)
