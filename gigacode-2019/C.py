D = int(input())
total = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = float('inf')
for i in range(D):
    total += a[i]
    if total >= b[i] and b[i] < ans:
        ans = b[i]
if ans == float('inf'):
    print(-1)
else:
    print(ans)
