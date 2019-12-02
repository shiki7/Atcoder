n = int(input())
a = [[i, int(input())] for i in range(n)]

sorted_a = sorted(a, key=lambda x: x[1])

index = 0
cur = sorted_a[0][1]
for i in range(n):
    if sorted_a[i][1] == cur:
        sorted_a[i][1] = index
    else:
        index += 1
        cur = sorted_a[i][1]
        sorted_a[i][1] = index

b = sorted(sorted_a, key=lambda x: x[0])

for i in range(n):
    print(b[i][1])
