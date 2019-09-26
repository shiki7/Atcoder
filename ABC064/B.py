n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(1, n):
    total += abs(a[i] - a[i - 1])
print(total)
