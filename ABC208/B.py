p = int(input())
a = [1]
for i in range(1, 10):
    a.append(a[i - 1] * (i + 1))
a.reverse()
ans = 0
for i in range(10):
    if p >= a[i]:
        ans += p // a[i]
        p %= a[i]
print(ans)