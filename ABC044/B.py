import collections

w = input()
c = collections.Counter(w)
for k, v in c.items():
    if v % 2 == 1:
        print('Not')
        exit()
print('Yes')
