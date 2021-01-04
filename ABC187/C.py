N = int(input())
s = list(input() for _ in range(N))
S = set(s)
for a in S:
    if a[0] != "!" and ("!" + a) in S:
        print(a)
        exit()
print("satisfiable")
