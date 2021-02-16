N = int(input())
for i in range(N):
    L, R = map(int, input().split())
    x = R - L*2
    if x < 0:
        print(0)
    else:
        print((x+1)*(x+2)//2)
