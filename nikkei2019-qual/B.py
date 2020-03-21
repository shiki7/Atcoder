N = int(input())
a = [input() for _ in range(3)]
ans = 0
for i in range(N):
    ans += len(set([a[0][i], a[1][i], a[2][i]])) - 1
print(ans)
