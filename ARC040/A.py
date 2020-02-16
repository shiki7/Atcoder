n = int(input())
s = [list(input()) for _ in range(n)]
red = 0
blue = 0
for i in range(n):
    red += s[i].count('R')
    blue += s[i].count('B')
if red > blue:
    print('TAKAHASHI')
elif red == blue:
    print('DRAW')
else:
    print('AOKI')
