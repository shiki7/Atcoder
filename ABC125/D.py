n = int(input())
a = list(map(int, input().split()))
ne_num = 0

for i in range(n):
    if a[i] < 0:
        ne_num += 1
if ne_num % 2 == 0:
    print(sum(list(map(abs, a))))
    exit()

min_b = 10**9
for i in range(n):
    if abs(a[i]) < min_b:
        min_b = abs(a[i])
print(sum(list(map(abs, a))) - 2*min_b)
