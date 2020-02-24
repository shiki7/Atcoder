c = int(input())
nml = [list(map(int, input().split())) for _ in range(c)]
max1, max2, max3 = 0, 0, 0
for i in range(c):
    tmp = sorted(nml[i])
    max1 = max(max1, tmp[0])
    max2 = max(max2, tmp[1])
    max3 = max(max3, tmp[2])
print(max1*max2*max3)
