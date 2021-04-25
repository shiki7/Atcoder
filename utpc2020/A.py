# pypyじゃないとTLE
N, L = map(int, input().split())
X, A = [], []
for _ in range(N):
    x, a = map(int, input().split())
    X.append(x)
    A.append(a)
le, ri = 0, 2*10**14
while ri-le > 1:
    mid = (le+ri)//2
    total = (le+ri)//2
    pos = 0
    flag = True
    for i in range(N):
        total = min(mid, total+X[i] - pos)
        total -= A[i]
        if total < 0:
            flag = False
            break
        pos = X[i]
    if flag:
        ri = mid
    else:
        le = mid
print(ri)
