w, a, b = map(int, input().split())
ans = abs(a - b) - w
if ans < 0:
    print(0)
else:
    print(ans)
