N = int(input())
if N % 4 == 0 or N % 7 == 0:
    print('Yes')
    exit()
for i in range(N // 4 + 1):
    for j in range(N // 7 + 1):
        if 4 * i + 7 * j == N:
            print('Yes')
            exit()
print('No')
