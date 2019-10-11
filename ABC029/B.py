s = [input() for _ in range(12)]
ans = 0
for w in s:
    if 'r' in w:
        ans += 1
print(ans)
