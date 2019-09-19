n = int(input())
sp = [[i + 1, input().split()] for i in range(n)]
sp = sorted(sp, key=lambda x: (x[1][0], -int(x[1][1])))
for k, v in sp:
    print(k)
