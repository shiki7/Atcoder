N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
for i in range(len(ab)):
    print(ab[i][0] % ab[i][1])
