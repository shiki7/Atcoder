A, B, C, D = map(int, input().split())
E = list(list(map(int, input().split())) for _ in range(C))
p = []
for i in range(C):
    sorted_e = sorted(E[i], reverse=True)
    p.append(sorted_e[B-1])
p = sorted(p, reverse=True)
print(p[D-1])
