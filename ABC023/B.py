n = int(input())
s = input()

ans = 'b'

if s == 'b':
    print(0)
    exit()

for i in range(1, n):
    if i % 3 == 1:
        ans = 'a' + ans + 'c'
    elif i % 3 == 2:
        ans = 'c' + ans + 'a'
    elif i % 3 == 0:
        ans = 'b' + ans + 'b'
    if ans == s:
        print(i)
        exit()
print(-1)
