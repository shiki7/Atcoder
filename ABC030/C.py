n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

time = 0
ans = 0
i = j = 0
while True:
    while i < len(a) and a[i] < time:
        i += 1
    if i == len(a):
        break
    time = a[i] + x
    while j < len(b) and b[j] < time:
        j += 1
    if j == len(b):
        break
    time = b[j] + y
    ans += 1
print(ans)
