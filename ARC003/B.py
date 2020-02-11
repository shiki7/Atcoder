n = int(input())
s = [input()[::-1] for _ in range(n)]
s = sorted(s)
for i in range(n):
    print(s[i][::-1])
