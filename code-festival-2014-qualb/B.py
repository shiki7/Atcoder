n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

total = 0
for i in range(n):
    total += a[i]
    if total >= k:
        print(i+1)
        exit()
