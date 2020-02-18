from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted(a)
c = sorted(c)
ans = 0
for i in range(n):
    ans += (bisect_left(a, b[i])) * (n - bisect_right(c, b[i]))
print(ans)
