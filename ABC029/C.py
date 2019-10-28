import itertools

n = int(input())
for x in itertools.product('abc', repeat=n):
    print(''.join(x))
