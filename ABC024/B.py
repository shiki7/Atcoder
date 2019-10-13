n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = t
for i in range(1, n):
    # ドアが開いているとき
    if a[i-1] + t > a[i]:
        ans += a[i] - a[i-1]
    else:
        ans += t
print(ans)
