a, b, c = map(int, input().split())
for i in range(10**3):
    if (c+60*i) % (a+b) <= a:
        print(c+60*i)
        exit()
print(-1)
