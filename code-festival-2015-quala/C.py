import heapq

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

sum_a = 0
diff = []
heapq.heapify(diff)
for i in range(N):
    heapq.heappush(diff, AB[i][1] - AB[i][0])
    sum_a += AB[i][0]
    
if sum_a <= T:
    print(0)
    exit()

for i in range(1, N+1):
    sum_a += heapq.heappop(diff)
    if sum_a <= T:
        print(i)
        exit()
print(-1)
