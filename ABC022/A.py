n, s, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
count = 0
w = 0
for num in a:
    w += num
    if s <= w <= t:
        count += 1
print(count)
