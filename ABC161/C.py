n, k = map(int, input().split())
print(min(n % k, (n//k + 1) * k - n))
