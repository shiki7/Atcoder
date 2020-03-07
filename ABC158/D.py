import sys
input = sys.stdin.readline

S = input().rstrip()
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

ans = S
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
            ans = c + ans
        elif f == '1' and not flag:
            ans = ans + c
        elif f == '2' and flag:
            ans = ans + c
        elif f == '2' and not flag:
            ans = c + ans
if flag:
    print(ans)
else:
    print(ans[::-1])
