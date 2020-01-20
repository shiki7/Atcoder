n, k = map(int, input().split())

# a + b = kx
# b + c = ky
# c + a = kz
# a = k(x-y+z)/2

div = n // k
# kが奇数のとき,(a,b,c)はそれぞれkで割った余りは0になる
if k % 2 == 1:
    print(div ** 3)
# kが偶数のとき,(1) + (2)を足したもの
# (1) (a,b,c)それぞれkで割った余りが0
# (2) k/2余る
else:
    if div * k + k/2 <= n:
        print(div**3 + (div+1)**3)
    else:
        print(2*(div**3))
