import itertools

n = int(input())
a = [i+1 for i in range(n)]

p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = []
for i, v in enumerate(itertools.permutations(a, n)):
    if list(v) == p or list(v) == q:
        ans.append(i)
    if len(ans) == 2:
        print(ans[1] - ans[0])
        exit()
print(0)
