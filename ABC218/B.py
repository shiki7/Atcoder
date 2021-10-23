p = list(map(int, input().split()))
ans = []
for i in range(26):
    ans.append(chr(p[i]+96))
print(''.join(ans))
