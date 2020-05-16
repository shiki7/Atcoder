from collections import Counter
n = int(input())
s = input().split()
ans = 0
for i in range(n):
    if s[i].upper() == 'TAKAHASHIKUN' or s[i].upper() == 'TAKAHASHIKUN.':
        ans += 1
print(ans)
