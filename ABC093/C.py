a = list(map(int, input().split()))

a.sort()
ans = 0
ans += a[2] - a[1]
diff = a[2] - (a[0] + (a[2] - a[1]))
if diff % 2 == 0:
    ans += diff // 2
else:
    ans += diff // 2 + 2
print(ans)
