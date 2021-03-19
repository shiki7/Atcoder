from itertools import product


def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


N = int(input())
S = list(map(int, input().split()))
A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

P = product([0, 1], repeat=len(A))
ans = float('inf')
for p in P:
    x = 1
    for i in range(len(p)):
        if p[i] == 1:
            x *= A[i]
    if x == 1:
        continue
    flg = True
    for s in S:
        if gcd(s, x) == 1:
            flg = False
            break
    if flg:
        ans = min(ans, x)
print(ans)
