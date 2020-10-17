n = int(input())
s = [input() for _ in range(n)]
a = []
for i in range(n):
    for j in range(i+1, n):
        a.append(s[i]+s[j])
        a.append(s[j]+s[i])
a = sorted(a)
print(a[0])
