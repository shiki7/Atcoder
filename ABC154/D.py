n, k = map(int, input().split())
p = list(map(int, input().split()))

total = [0]
for i in range(1, 200000):
    total.append(total[i-1]+i)

ans_index = 0
cur = sum(p[0:k])
max_p = cur
for i in range(n-k+1):
    cur = cur + p[i+k-1] - p[i-1]
    if cur > max_p:
        max_p = cur
        ans_index = i
ans = 0
for i in range(k):
    ans += total[p[ans_index+i]] / p[ans_index+i]
print(ans)
