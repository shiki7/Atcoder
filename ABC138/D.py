import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
 
 
def dfs(cur, par):
    for child in edge[cur]:
        if child == par:
            continue
        counter[child] += counter[cur]
        dfs(child, cur)
 
 
N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N-1)]
px = [list(map(int, input().split())) for _ in range(Q)]
counter = [0] * N
 
edge = [[] for _ in range(N)]
for i in range(N-1):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    edge[a].append(b)
    edge[b].append(a)
 
for i in range(Q):
    p = px[i][0] - 1
    x = px[i][1]
    counter[p] += x
 
 
dfs(0, -1)
print(*counter)
