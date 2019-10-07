import math
n = int(input())
max_num = math.ceil(math.sqrt(n))
ans = 100000
for w in range(1, max_num + 1):
    for h in range(w, n + 1):
        if w * h > n:
            break
        ans = min(ans, n - w * h + (h - w))
print(ans)
