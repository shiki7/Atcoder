m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

if m1 == m2:
    print(d2-d1)
    exit()


day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = 0
for i in range(m1, m2+1):
    if i == m1:
        ans += day[i-1] - d1
    elif i == m2:
        ans += d2
        break
    else:
        ans += day[i-1]
print(ans)
