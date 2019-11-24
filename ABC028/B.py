import collections
s = input()
chars = ['A', 'B', 'C', 'D', 'E', 'F']

counter = collections.Counter(s)

ans = []
for char in chars:
    ans += [counter[char]]
print(' '.join(map(str, ans)))
