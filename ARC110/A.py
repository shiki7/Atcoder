def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = x * a[i] // gcd(x, a[i])
    return x


N = int(input())
arr = []
for i in range(2, N+1):
    arr.append(i)
print(lcm(arr)+1)
