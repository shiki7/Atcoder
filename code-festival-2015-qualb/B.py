import collections

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = collections.Counter(a)
mc = c.most_common()[0]
if mc[1] > n/2:
    print(mc[0])
else:
    print('?')
