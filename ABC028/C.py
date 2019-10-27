a = list(map(int, input().split()))
a = sorted(a, reverse=True)
print(max(a[0] + a[1] + a[4], a[0] + a[2] + a[3]))
