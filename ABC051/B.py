k, s = map(int, input().split())
count = 0
for a in range(k + 1):
    for b in range(k + 1):
        if 0 <= s - (a + b) <= k:
            count += 1
print(count)
