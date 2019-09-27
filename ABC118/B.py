n, m = map(int, input().split())
ka = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(ka[0][0])
    exit()

counter = [0] * m
for x in ka:
    for a in x[1:]:
        counter[a - 1] += 1
ans = 0
for i in range(m):
    if counter[i] == n:
        ans += 1
print(ans)
