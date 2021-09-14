N = int(input())
a = list(map(int, input().split()))
b = sorted(a)
for i in range(N):
    if a[i] == b[-2]:
        print(i + 1)
