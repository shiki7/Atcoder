n = int(input())
sp = [list(input().split()) for _ in range(n)]

total = 0
for s, p in sp:
    total += int(p)
for s, p in sp:
    if int(p) > total // 2:
        print(s)
        exit()
print('atcoder')
