b = list(map(int, input().split()))
n = int(input())
c = []
for i in range(n):
    s = input()
    t = []
    for j in range(len(s)):
        t.append(str(b.index(int(s[j]))))
    c.append(int(''.join(t)))
c = sorted(c)
for i in range(n):
    s = str(c[i])
    t = []
    for j in range(len(s)):
        t.append(str(b[int(s[j])]))
    print(''.join(t))
