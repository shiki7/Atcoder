N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

total = 0
for i in range(N):
    total += b[a[i]-1]
    if i >= 1 and a[i-1] + 1 == a[i]:
        total += c[a[i-1]-1]
print(total)
