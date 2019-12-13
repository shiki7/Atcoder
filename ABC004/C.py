n = int(input())
a = ['1', '2', '3', '4', '5', '6']
n %= 30
for i in range(n):
    tmp = a[i % 5]
    a[i % 5] = a[i % 5 + 1]
    a[i % 5 + 1] = tmp
print(''.join(a))
