a, b, k = map(int, input().split())
if a >= k:
    print(a-k, b)
elif a < k and k-a <= b:
    print(0, b-(k-a))
else:
    print(0, 0)
