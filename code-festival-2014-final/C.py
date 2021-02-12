N = int(input())
for i in range(10, 10**5+1):
    str_i = str(i)
    total = 0
    for j in range(len(str_i)):
        total += int(str_i[-j-1]) * (i**j)
    if total == N:
        print(i)
        exit()
print(-1)
