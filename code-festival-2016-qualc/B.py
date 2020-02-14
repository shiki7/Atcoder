k, t = map(int, input().split())
a = list(map(int, input().split()))
max_a = max(a)
others = k-max_a
print(max(max_a - 1 - others, 0))
