from itertools import permutations

n = int(input())
c = input()
d = [i+j for i in "ABXY" for j in "ABXY"]

ans = float('INF')
for key in permutations(d, 2):
    ans = min(ans, len(c.replace(key[0], "L").replace(key[1], "R")))
print(ans)
