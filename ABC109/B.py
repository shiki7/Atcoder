n = int(input())
w = [input() for _ in range(n)]

if len(set(w)) is not n:
    print('No')
    exit()

for i in range(len(w) - 1):
    if not w[i][-1] == w[i + 1][0]:
        print('No')
        exit()
print('Yes')
