n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = sorted(a & b)
for i in range(len(c)):
    print(c[i])
