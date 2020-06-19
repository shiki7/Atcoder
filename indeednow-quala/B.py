N = int(input())
s = [input() for _ in range(N)]
w = sorted('indeednow')
for i in range(N):
    if sorted(s[i]) == w:
        print('YES')
    else:
        print('NO')
