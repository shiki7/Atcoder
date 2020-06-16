x, y = map(int, input().split())
for i in range(x+1):
    if y == i*4 + 2*(x-i):
        print('Yes')
        exit()
print('No')
