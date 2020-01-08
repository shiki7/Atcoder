n = int(input())
hl = [list(map(float, input().split())) for _ in range(n)]
count = [0 for _ in range(6)]
for high, low in hl:
    if high >= 35:
        count[0] += 1
    if 30 <= high < 35:
        count[1] += 1
    if 25 <= high < 30:
        count[2] += 1
    if low >= 25:
        count[3] += 1
    if low < 0 and high >= 0:
        count[4] += 1
    if high < 0:
        count[5] += 1
print(' '.join(map(str, count)))
