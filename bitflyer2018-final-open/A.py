n = int(input())
p = [input() for _ in range(n)]
ans = float('inf')
for i in range(n):
    for j in range(1, len(p[i])+1):
        if p[i][-j] != '0':
            ans = min(ans, j-1)
            break
print(ans)
