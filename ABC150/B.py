import re

n = int(input())
s = input()
result = re.findall('ABC', s)
print(len(result))
