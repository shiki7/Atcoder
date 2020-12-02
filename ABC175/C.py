X, K, D = map(int, input().split())
if X >= 0:
    if X // D >= K:
        print(X-D*K)
    else:
        if (K - X//D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))
elif X < 0:
    if abs(X) // D >= K:
        print(abs(X+D*K))
    else:
        if (K - abs(X)//D) % 2 == 0:
            print(abs(abs(X) % D))
        else:
            print(abs(abs(X) % D - D))
