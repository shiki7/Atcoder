n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(1, n):
    total += a[i] - a[i-1]
print(total/(n-1))
