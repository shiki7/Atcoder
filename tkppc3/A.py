a = [list(input().split()) for _ in range(2)]
if a[0][0] == a[1][0]:
    print(abs(int(a[0][1]) - int(a[1][1])) // 15)
else:
    print((int(a[0][1]) + int(a[1][1])) // 15)
