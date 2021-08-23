N, X = map(int, input().split())
a = list(map(int, input().split()))
if X >= sum(a) - N // 2:
    print('Yes')
else:
    print('No')
