n = int(input())
a = list(map(int, input().split()))

count = 1
is_up = False
is_down = False
for i in range(1, n):
    if a[i] < a[i-1] and is_up:
        count += 1
        is_up = False
    elif a[i] > a[i-1] and is_down:
        count += 1
        is_down = False
    elif a[i] < a[i-1]:
        is_down = True
    elif a[i] > a[i-1]:
        is_up = True
print(count)
