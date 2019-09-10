N, X = map(int, input().split())
x = list(map(int, input().split()))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


y = [abs(X - x[0])]
for i in range(len(x) - 1):
    y.append(abs(x[i + 1] - x[i]))

ans = y[0]
for i in range(1, len(y)):
    ans = gcd(ans, y[i])
print(ans)
