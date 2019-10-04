s = input()
t = ''
add_list = ['dream', 'dreamer', 'erase', 'eraser']
cur = len(s)
for i in range(len(s)):
    if s[-1 - i:cur] in add_list:
        cur = -1 - i
if -cur == len(s):
    print('YES')
else:
    print('NO')
