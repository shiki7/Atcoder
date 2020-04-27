n = int(input())
k = list(map(int, input().split()))
a = [k[0]]
for i in range(n-2):
    a.append(min(k[i], k[i+1]))
a.append(k[-1])
print(*a)
