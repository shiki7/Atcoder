import math
s = input()
s = int(s.replace(" ", ""))
if int(math.sqrt(s))**2 == s:
    print('Yes')
else:
    print('No')
