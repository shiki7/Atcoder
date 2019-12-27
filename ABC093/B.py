a, b, k = map(int, input().split())
if b-a <= k:
    for i in range(a, b+1):
        print(i)
    exit()
for i in range(a, a+k):
    print(i)
for i in range(max(a+k, b-k+1), b+1):
    print(i)
