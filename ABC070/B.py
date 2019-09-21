a, b, c, d = map(int, input().split())
diff = min(b, d) - max(a, c)
if diff <= 0:
    print(0)
else:
    print(diff)
