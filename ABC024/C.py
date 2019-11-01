n, d, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    s = st[i][0]
    t = st[i][1]
    if s < t:
        for j in range(d):
            if lr[j][0] <= s <= lr[j][1]:
                if t > lr[j][1]:
                    s = lr[j][1]
                else:
                    print(j+1)
                    break
    else:
        for j in range(d):
            if lr[j][0] <= s <= lr[j][1]:
                if t < lr[j][0]:
                    s = lr[j][0]
                else:
                    print(j+1)
                    break
