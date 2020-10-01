n = int(input())
s = input()
d = [0]*4
for i in range(n):
    d[int(s[i])-1] += 1
print(max(d), min(d))
