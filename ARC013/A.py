a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)

if a[0] < b[0] or a[1] < b[1] or a[2] < b[2]:
    print(0)
else:
    print(max(
        (a[0]//b[0]) * (a[1]//b[1]) * (a[2]//b[2]),
        (a[0]//b[0]) * (a[1]//b[2]) * (a[2]//b[1]),
        (a[0]//b[1]) * (a[1]//b[0]) * (a[2]//b[2]),
        (a[0]//b[1]) * (a[1]//b[2]) * (a[2]//b[0]),
        (a[0]//b[2]) * (a[1]//b[0]) * (a[2]//b[1]),
        (a[0]//b[2]) * (a[1]//b[1]) * (a[2]//b[0]))
    )
