def base_10_to_n(x, n):
    tmp = x
    res = ''
    while tmp > 0:
        res = str(tmp % n)+res
        tmp = int(tmp/n)
    return res


n, k = map(int, input().split())
print(len(str(base_10_to_n(n, k))))
