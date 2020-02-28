n = int(input())
x = list(map(int, input().split()))
mid = sum(x)//n
mid2 = mid + 1
ans = 0
ans2 = 0
for i in range(n):
    ans += (x[i] - mid) ** 2
    ans2 += (x[i] - mid2) ** 2
print(min(ans, ans2))
