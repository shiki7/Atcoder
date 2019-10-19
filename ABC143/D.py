# TLE not clear
import itertools

n = int(input())
L = list(map(int, input().split()))

ans = 0
L.sort()

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if L[k] < L[i]+L[j]:
                ans += 1
            else:
                break
print(ans)
