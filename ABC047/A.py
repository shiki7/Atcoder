a, b, c = map(int, input().split())
if a + b + c - max(a, b, c) == max(a, b, c):
    print('Yes')
else:
    print('No')
