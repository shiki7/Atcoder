import itertools
n = int(input())
s = input()


print(len(set(list(itertools.combinations(s, 3)))))
