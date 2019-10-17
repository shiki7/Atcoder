N, L = map(int, input().split())
s = [input() for _ in range(N)]
s.sort()
ans = ''
for x in s:
    ans += x
print(ans)
