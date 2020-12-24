n = int(input())
ans = 1
for i in range(n-1, n-1-11, -1):
    ans *= i
for j in range(11, 1, -1):
    ans //= j
print(ans)
