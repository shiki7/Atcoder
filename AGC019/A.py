Q, H, S, D = map(int, input().split())
N = int(input())
if N % 2 == 0:
    print((N//2)*min(Q*8, H*4, S*2, D))
else:
    print((N//2)*min(Q*8, H*4, S*2, D)+min(Q*4, H*2, S))
