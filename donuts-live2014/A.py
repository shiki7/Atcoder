N = int(input())
a = list(map(int, input().split()))
total = 0
if N % 2 == 1:
    print('error')
    exit()
for i in range(N//2):
    total += a[2*i+1] - a[2*i]
print(total)
