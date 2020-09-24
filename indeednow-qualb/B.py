s = input()
t = input()
if len(s) != len(t):
    print(-1)
elif s == t:
    print(0)
else:
    for i in range(1, len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print(i)
            exit()
    print(-1)
