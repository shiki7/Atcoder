n = int(input())
t = list(map(int, input().split()))
m = int(input())
pm = [list(map(int, input().split())) for _ in range(m)]

for p, m in pm:
    ans = 0
    for i in range(len(t)):
        if p-1 == i:
            ans += m
        else:
            ans += t[i]
    print(ans)
