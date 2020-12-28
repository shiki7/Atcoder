n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
mn = float("inf")
mx = 0
for i in range(n//2):
    sm = a[i] + a[n-i-1]
    mn = min(mn, sm)
    mx = max(mx, sm)
print(mx-mn)
