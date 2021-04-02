N = int(input())
S = input()

l = 0
r = 0

for i in range(N):
    if S[i] == '#':
        break
    l += 1

for i in range(N-1, -1, -1):
    if S[i] == '#':
        break
    r += 1

cnt = 0
mx = 0
for i in range(N):
    if S[i] == '.':
        cnt += 1
    else:
        cnt = 0
    mx = max(mx, cnt)
print(l, r + (max(0, mx - (l + r))))
