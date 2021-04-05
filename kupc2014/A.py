a = list(map(int, input().split()))
b = sorted(a[:3])
c = sorted(a[3:])
ans = 0
for i in range(3):
    ans += abs(b[i] - c[i])
print(ans)
