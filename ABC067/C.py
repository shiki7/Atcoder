n = int(input())
a = list(map(int, input().split()))
total = sum(a)
left = 0
ans = float('inf')
for i in range(n-1):
    left += a[i]
    ans = min(abs(total-2*left), ans)
print(ans)
