n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    if d % a[i] != 0:
        ans += d // a[i] + 1
    else:
        ans += d // a[i]
print(ans+x)
