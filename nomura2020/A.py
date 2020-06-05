h1, m1, h2, m2, k = map(int, input().split())
print(max(abs(60*h2+m2 - 60*h1-m1) - k, 0))
