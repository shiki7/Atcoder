A, B = map(int, input().split())
for i in range(100):
    if (A-1)*i + 1 >= B:
        print(i)
        exit()
