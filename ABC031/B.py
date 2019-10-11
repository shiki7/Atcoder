L, H = map(int, input().split())
N = int(input())
a = [int(input()) for _ in range(N)]
for i in range(N):
    if a[i] > H:
        print(-1)
    elif L <= a[i] <= H:
        print(0)
    else:
        print(L - a[i])
