n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
sorted_ab = sorted(ab, key=lambda x: x[1])

total = 0
for a, b in sorted_ab:
    total += a
    if total > b:
        print('No')
        exit()
print('Yes')
