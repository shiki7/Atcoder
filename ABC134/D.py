n = int(input())
a = list(map(int, input().split()))

b = [0] * n

for i in range(n, 0, -1):
    if sum(b[i-1::i]) % 2 == a[i-1]:
        continue
    else:
        b[i-1] = 1

c = []
for i in range(n):
    if b[i] == 1:
        c.append(i+1)
print(sum(b))
if len(c) > 0:
    print(*c)
