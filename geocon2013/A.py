data = [[int(x) for x in input().split()]+[i] for i in range(1, 301)]
data.sort()
ans = []
for i in range(100):
    ans.append(' '.join(str(c) for a, b, c in data[3*i:3*i+3]))
print(100)
print('\n'.join(ans))
