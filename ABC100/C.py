N = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    while i % 2 == 0:
        i //= 2
        count += 1
print(count)
