n = int(input())
xu = [input().split() for _ in range(n)]
ans = 0
for x, u in xu:
    if u == 'JPY':
        ans += float(x)
    else:
        ans += 380000 * float(x)
print(ans)
