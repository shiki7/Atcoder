import re
S = input()
if re.match(r'[0-9]{3}-[0-9]{4}', S):
    print('Yes')
else:
    print('No')
