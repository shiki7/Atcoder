A, B, K, L = map(int, input().split())

if B/L < A:
    print(min((K//L) * B + (K % L)*A, ((K//L)+1) * B))
else:
    print(A*K)
