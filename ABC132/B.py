n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    tmp = sorted(p[i-1:i+2])
    if p[i] == tmp[1]:
        count += 1
print(count)
