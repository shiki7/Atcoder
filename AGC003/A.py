s = list(input())
if len(set(s)) == 4:
    print('Yes')
elif len(set(s)) == 2:
    if ('S' in s and 'N' in s) or ('E' in s and 'W' in s):
        print('Yes')
    else:
        print('No')
else:
    print('No')
