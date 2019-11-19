import itertools

s = input()
n = int(input())
a = list(itertools.product(s, s))
print(''.join(a[n-1]))
