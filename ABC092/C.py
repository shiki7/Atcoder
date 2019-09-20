n = int(input())
a = [0] + list(map(int, input().split())) + [0]
# 累積和
cur = 0
b = []
for i in range(1, len(a)):
    b.append(abs(a[i] - cur))
    cur = a[i]
s = sum(b)

for i in range(1, n + 1):
    print(s + abs(a[i + 1] - a[i - 1]) - (abs(b[i - 1]) + abs(b[i])))
