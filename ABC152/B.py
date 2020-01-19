a, b = map(int, input().split())
c = str(a) * b
d = str(b) * a
if str(c) < str(d):
    print(c)
else:
    print(d)
