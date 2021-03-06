# union find
def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


def unite(x, y):
    '''x,yの属する集合の併合'''
    x = find_root(x)
    y = find_root(y)

    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1


N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(M)]

# 初期化
parent = [i for i in range(N)]  # 根
rank = [1] * N  # 深さ
size = [1] * N  # iを根とするグループのサイズ

# 連結
for i in range(M):
    unite(uv[i][0]-1, uv[i][1]-1)

# グループの合計が一致することを確認
x = [0] * N
y = [0] * N
for i in range(N):
    x[find_root(i)] += a[i]
    y[find_root(i)] += b[i]
for i in range(N):
    if x[i] != y[i]:
        print('No')
        exit()
print('Yes')
