import re

N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    if re.match(r'[a-z]*okyo[a-z]*ech[a-z]*', S[i]):
        print('Yes')
    else:
        print('No')
