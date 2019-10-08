def check(x, d):
    str_x = str(x)
    for s in str_x:
        if s in d:
            return False
    return True


n, k = map(int, input().split())
d = list(input().split())

for x in range(n, 10**10):
    if check(x, d):
        print(x)
        exit()
