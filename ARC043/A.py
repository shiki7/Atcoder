n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]

if len(set(s)) == 1:
    print(-1)
    exit()
s = sorted(s)
p = b / (s[-1] - s[0])
q = (a*n-p * sum(s))/n
print(p, q)
