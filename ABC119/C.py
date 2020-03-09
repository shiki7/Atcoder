N, A, B, C = map(int, input().split())
li = [int(input()) for _ in range(N)]


def dfs(cur, a, b, c):
    if cur == N:
        if min(a, b, c) > 0:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30
        else:
            return float('inf')
    ret0 = dfs(cur+1, a, b, c)
    ret1 = dfs(cur+1, a+li[cur], b, c) + 10
    ret2 = dfs(cur+1, a, b+li[cur], c) + 10
    ret3 = dfs(cur+1, a, b, c+li[cur]) + 10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
