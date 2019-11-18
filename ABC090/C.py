n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
elif n >= 2 and m == 1:
    print(n-2)
elif n == 1 and m >= 2:
    print(m-2)
elif n >= 2 and m >= 2:
    # 4隅が表、4隅以外の外周が表、それ以外が裏
    # つまり外周を取り除いたところが裏
    print((n-2)*(m-2))
