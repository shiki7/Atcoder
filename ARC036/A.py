n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
for i in range(n-2):
    if li[i] + li[i+1] + li[i+2] < k:
        print(i+3)
        exit()
print(-1)
