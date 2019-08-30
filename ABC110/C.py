import collections

S = input()
T = input()

s_counter = collections.Counter(S)
t_counter = collections.Counter(T)

if sorted(s_counter.values()) == sorted(t_counter.values()):
    print('Yes')
else:
    print('No')
