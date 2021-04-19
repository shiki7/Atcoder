def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


ans = 1
a, b = map(int, input().split())
for i in range(a, b):
    for j in range(i+1, b+1):
        ans = max(ans, gcd(i, j))
print(ans)
