# not fix

from collections import defaultdict


def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


# x,yの属する集合の併合
def unite(x, y):
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

# xとyが同じグループかどうか判定


def same(x, y):
    return find_root(x) == find_root(y)


dic = defaultdict(list)

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

for i in range(m):
    a = ab[i][0]
    b = ab[i][1]
    dic[a].append(b)
    dic[b].append(a)
for i in range(k):
    c = cd[i][0]
    d = cd[i][1]
    dic[c].append(d)
    dic[d].append(c)

parent = [i for i in range(n)]  # 根
rank = [1] * n  # 深さ
size = [1] * n  # iを根とするグループのサイズ

edge = [[ab[m - 1 - i][0] - 1, ab[m - 1 - i][1] - 1] for i in range(m)]

res = []
for i in range(m):
    a = find_root(edge[i][0])
    b = find_root(edge[i][1])
    if a == b:
        res.append(0)
    else:
        res.append(size[a] * size[b])
        unite(a, b)
print(edge)
print(size)
ans = []
for i in range(n):
    ans.append(size[i] - len(dic[i+1]))
print(' '.join(map(str, ans)))
