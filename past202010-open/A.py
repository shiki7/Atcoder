a = list(map(int, input().split()))
b = ['A', 'B', 'C']
for i in range(3):
    if a[i] == sorted(a)[1]:
        print(b[i])
