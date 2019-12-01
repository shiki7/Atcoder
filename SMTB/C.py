x = int(input())
count = x // 100
a = x - count * 100
if a / 5 <= count:
    print("1")
else:
    print("0")
