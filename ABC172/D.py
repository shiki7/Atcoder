n = int(input())
ans = 0
for i in range(1, n+1):
    y = n // i
    ans += y*(y+1)*i // 2
print(ans)
