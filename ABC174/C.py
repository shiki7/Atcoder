K = int(input())

t = 7 % K
if t == 0:
    print(1)
    exit()
for i in range(2, 10**6):
    t = (t * 10 + 7) % K
    if t == 0:
        print(i)
        exit()
print(-1)
