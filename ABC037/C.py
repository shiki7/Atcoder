n, k = map(int, input().split())
a = list(map(int, input().split()))

prev = sum(a[0:k])
total = prev
for i in range(1, n - k + 1):
    prev = prev - a[i - 1] + a[i + k - 1]
    total += prev
print(total)
