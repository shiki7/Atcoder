n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]

# aが大きい順に並び替え
ab = sorted(ab, reverse=True)
# dが小さい順に並び替え
cd = sorted(cd, key=lambda x: x[1])

count = 0
for a, b in ab:
    for c, d in cd:
        if a < c and b < d:
            count += 1
            cd.remove([c, d])
            break
print(count)
