from itertools import permutations

y, m, d = input().split("/")
a = [m[0], m[1], d[0], d[1]]
for s in permutations(a):
    if y == ''.join(list(s)):
        print('yes')
        exit()
print('no')
