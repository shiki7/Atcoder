X, K = map(int, input().split())
if K == 0:
    print(X+1)
else:
    if len(str(X)) < K+1:
        print('1'+'0' * K)
    else:
        a = int(str(X)[:-K]) + 1
        print(str(a) + '0' * K)
