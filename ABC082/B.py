s = list(input())
s = sorted(s)
s = ''.join(s)

t = list(input())
t = sorted(t, reverse=True)
t = ''.join(t)

if s < t:
    print('Yes')
else:
    print('No')
