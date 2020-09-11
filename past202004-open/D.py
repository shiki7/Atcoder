import re

s = input()
li = 'abcdefghijklmnopqrstuvwxyz.'

y = set()
for i in range(27):
    for j in range(27):
        for k in range(27):
            x = li[i]+li[j]+li[k]
            for a in range(3):
                if re.search(x[:a+1], s):
                    y.add(x[:a+1])
print(len(y))
