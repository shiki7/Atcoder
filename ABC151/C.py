n, m = map(int, input().split())
ps = [input().split() for _ in range(m)]

ps = sorted(ps, key=lambda x: x[0])

flag = 0
wa = {}
AC_count = 0
WA_count = 0
for i in range(m):
    if ps[i][0] != flag:
        if ps[i][1] == 'AC':
            AC_count += 1
            if ps[i][0] in wa.keys():
                WA_count += wa[ps[i][0]]
            flag = ps[i][0]
        else:
            if ps[i][0] in wa.keys():
                wa[ps[i][0]] += 1
            else:
                wa[ps[i][0]] = 1
print(AC_count, WA_count)
