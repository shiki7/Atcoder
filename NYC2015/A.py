n = int(input())
s = str(bin(n))[2:]
if s == s[::-1]:
    print('Yes')
else:
    print('No')
