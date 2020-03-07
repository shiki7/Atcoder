import sys
input = sys.stdin.readline

S = input().rstrip()
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

a = ''
ans = S
b = ''
flag = True

for i in range(Q):
    if query[i][0] == '1':
        if flag:
            flag = False
        else:
            flag = True
        continue
    elif query[i][0] == '2':
        f = query[i][1]
        c = query[i][2].rstrip()
        if f == '1' and flag:
            a = c + a
        elif f == '1' and not flag:
            b = b + c
        elif f == '2' and flag:
            b = b + c
        elif f == '2' and not flag:
            a = c + a
if flag:
    print(a + ans + b)
else:
    tmp = a + ans + b
    print(tmp[::-1])
