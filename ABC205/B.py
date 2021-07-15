N = int(input())
a = list(map(int, input().split()))
if len(set(a)) == N and max(a) == N and min(a) == 1:
    print('Yes')
else:
    print('No')
