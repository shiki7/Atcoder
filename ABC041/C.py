n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([i, a[i]])
b = sorted(b, key=lambda x: x[1], reverse=True)
for i in range(n):
    print(b[i][0] + 1)
    
