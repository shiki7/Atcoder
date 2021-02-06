N, K = map(int, input().split())
if K <= N:
    print(K**3)
elif K <= 2*N:
    print(K**3-3*((K-N)**3))
elif K <= 3*N:
    print(N**3*6-(3*N-K)**3)
else:
    print(N**3*6)
