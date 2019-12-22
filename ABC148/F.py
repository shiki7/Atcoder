# not complete
n, u, v = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n-1)]

node = [[0] for _ in range(n+1)]
print(node)
for i in range(n-1):
    node[ab[i][0]].append(ab[i][1])
    node[ab[i][1]].append(ab[i][0])
print(node)

dummy = 10**6
# 青木くんの初期位置を0としてノードのrankを求める
rank = [dummy for _ in range(n+1)]
rank[u] = 0
