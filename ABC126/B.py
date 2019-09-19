s = input()
a = int(s[0:2])
b = int(s[2:4])

if a <= 12 and b <= 12 and a != 0 and b != 0:
    print('AMBIGUOUS')
elif (a > 12 and 0 < b <= 12) or (a == 0 and 0 < b <= 12):
    print('YYMM')
elif (0 < a <= 12 and b > 12) or (0 < a <= 12 and b == 0):
    print('MMYY')
else:
    print('NA')
