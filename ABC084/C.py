n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]

for j in range(n-1):
    time = 0
    for i in range(j, n-1):
        c = csf[i][0]
        s = csf[i][1]
        f = csf[i][2]
        if time <= s:
            time = s+c
        else:
            if (time - s) % f == 0:
                time += c
            else:
                time += (f - (time - s)) % f + c
    print(time)
print(0)
