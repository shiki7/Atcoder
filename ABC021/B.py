n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

if len(set(p)) == k and a not in p and b not in p:
    print('YES')
else:
    print('NO')
