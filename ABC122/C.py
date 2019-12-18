n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]
t = [0]
count = 0
for i in range(1, n):
    if s[i-1] + s[i] == 'AC':
        count += 1
    t.append(count)
for le, ri in lr:
    print(t[ri-1] - t[le-1])
