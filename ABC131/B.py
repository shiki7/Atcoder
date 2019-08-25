N, L = map(int, input().split())
p_list = []
for i in range(1, N+1):
    p_list += [L + i - 1]
print(sum(p_list) - sorted(p_list, key=abs)[0])
