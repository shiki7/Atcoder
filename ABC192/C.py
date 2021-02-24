def calc(x):
    a = list(str(x))
    return int(''.join(sorted(a, reverse=True))) - int(''.join(sorted(a)))


n, k = map(int, input().split())
for i in range(k):
    n = calc(n)
print(n)
