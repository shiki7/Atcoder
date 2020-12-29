
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


def same(x, y):
    '''xとyが同じグループかどうか判定'''
    return find_root(x) == find_root(y)


# 入力
N, Q = map(int, input().split())
tuv = [list(map(int, input().split())) for _ in range(Q)]

# 初期化
parent = [i for i in range(N)]  # 根
rank = [1] * N  # 深さ
size = [1] * N  # iを根とするグループのサイズ

for i in range(Q):
    if tuv[i][0] == 0:
        unite(tuv[i][1], tuv[i][2])
    else:
        if same(tuv[i][1], tuv[i][2]):
            print(1)
        else:
            print(0)
