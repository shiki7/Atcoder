import math
n = int(input())
a = list(map(int, input().split()))

b = sum(a) / n
ceil = math.ceil(b)
floor = math.floor(b)

ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += (a[i] - ceil)**2
for i in range(n):
    ans2 += (a[i] - floor)**2
print(min(ans1, ans2))
