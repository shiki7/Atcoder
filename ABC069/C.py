n = int(input())
a = list(map(int, input().split()))

count4 = 0
count2_except4 = 0
for i in range(n):
    if a[i] % 4 == 0:
        count4 += 1
    elif a[i] % 2 == 0:
        count2_except4 += 1
if count4 * 2 + 1 >= n:
    print('Yes')
elif count2_except4 >= n - 2 * count4:
    print('Yes')
else:
    print('No')
