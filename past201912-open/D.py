from collections import defaultdict
d = defaultdict(lambda: 0)

n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    d[a[i]] += 1
if len(d) == n:
    print('Correct')
    exit()

for i in range(1, n+1):
    if i not in d:
        ans1 = i
    if d[i] == 2:
        ans2 = i
print(ans2, ans1)
