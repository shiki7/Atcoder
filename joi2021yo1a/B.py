n = int(input())
s = input()
d = {'J': 0, 'O': 0, 'I': 0}
for i in range(n):
    d[s[i]] += 1
print('J'*d['J'] + 'O'*d['O'] + 'I' * d['I'])
