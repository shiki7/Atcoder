n = int(input())
if (n-1) // 20 % 2 == 0:
    if n % 20 == 0:
        print(20)
    else:
        print(n % 20)
else:
    print(20-(n-1) % 20)
