n = int(input())
a = [int(input()) for _ in range(n)]
max_a = max(a)
a.sort(reverse=True)
for i in range(n):
    if a[i] != max_a:
        print(a[i])
        exit()
