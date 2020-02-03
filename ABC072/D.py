n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n):
    if i != n-1 and p[i] == i+1:
        p[i+1], p[i] = p[i], p[i+1]
        count += 1
    elif i == n-1 and p[i] == i+1:
        p[i-1], p[i] = p[i], p[i-1]
        count += 1
print(count)
