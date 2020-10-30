from collections import defaultdict
d = defaultdict(int)

n = int(input())
a = list(list(map(int, input().split())) for _ in range(n*(n-1)//2))
for i in range(n*(n-1)//2):
    if a[i][2] < a[i][3]:
        d[a[i][1]-1] += 3
    elif a[i][2] > a[i][3]:
        d[a[i][0]-1] += 3
    else:
        d[a[i][0]-1] += 1
        d[a[i][1]-1] += 1
sv = sorted(d.values(), reverse=True)
for i in range(n):
    for j in range(n):
        if d[i] == sv[j]:
            print(j+1)
            break
