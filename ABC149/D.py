n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

ans = 0
for i in range(n):
    if t[i] == 'r':
        ans += p
        if i+k < n and t[i+k] == 'r':
            t[i+k] = '0'
    elif t[i] == 's':
        ans += r
        if i+k < n and t[i+k] == 's':
            t[i+k] = '0'
    elif t[i] == 'p':
        ans += s
        if i+k < n and t[i+k] == 'p':
            t[i+k] = '0'
print(ans)
