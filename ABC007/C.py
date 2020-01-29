# bfs
from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

def bfs(sy, sx):
    # 未探索ステータス-1で初期化しておく
    dist = [[-1] * C for _ in range(R)]
    dist[sy][sx] = 0
    dq = deque()
    dq.append((sy, sx))
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if c[ny][nx] == '#' or dist[ny][nx] != -1:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                if ny == gy and nx == gx:
                    return dist[ny][nx]
                dq.append((ny, nx))
    return False
print(bfs(sy, sx))
