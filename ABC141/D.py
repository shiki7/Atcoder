# not clear
import numpy as np

N, M = map(int, input().split())
a = np.array(list(map(int, input().split())))

if N == 1:
    for i in range(M):
        a //= 2
    print(a[0])
    exit()

a.sort()
cur = M - 1
for i in range(M):
    if i == 0:
        a[-1] //= 2
    else:
        if (a[cur-1] > a[cur]):
            cur -= 1
            a[a[cur:].argmax()+cur] //= 2
        else:
            if cur == M-1:
                a[-1] //= 2
            else:
                a[a[cur:].argmax()+cur] //= 2
print(sum(a))
