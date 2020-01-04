r, g, b, n = map(int, input().split())

ans = 0
for i in range(n//r+1):
    for j in range(n//g+1):
        if r*i + g*j > n:
            break
        if (n - r*i - g*j) == 0 or ((n - r*i - g*j) >= b and (n - r*i - g*j) % b == 0):
            ans += 1
print(ans)
