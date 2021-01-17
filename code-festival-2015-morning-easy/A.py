N = int(input())
for i in range(101):
    if i**2 >= N:
        print(i**2-N)
        exit()
