from collections import defaultdict


def calc(x):
    return x*(x-1)//2


N = int(input())
A = list(map(int, input().split()))

dd = defaultdict(int)
for i in range(N):
    dd[A[i]] += 1

count = 0
for k, v in dd.items():
    if v >= 2:
        count += calc(v)
for i in range(N):
    ans = 0
    if dd[A[i]] >= 3:
        ans = count - calc(dd[A[i]]) + calc(dd[A[i]]-1)
    elif dd[A[i]] == 2:
        ans = count - 1
    elif dd[A[i]] == 1:
        ans = count
    print(ans)
