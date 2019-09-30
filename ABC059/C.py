n = int(input())
a = list(map(int, input().split()))


def check(op):  # 最初の数の正負を引数とする
    total = 0
    ans = 0
    for i in range(0, n):
        if (total+a[i]) > 0 and op == "+":
            ans += abs(-1 - (total + a[i]))
            total = -1
            op = "-"
        elif (total+a[i]) < 0 and op == "-":
            ans += abs(1 - (total + a[i]))
            total = 1
            op = "+"
        elif total+a[i] == 0:
            ans += 1
            if op == "+":
                total = -1
                op = "-"
            else:
                total = 1
                op = "+"
        else:
            total += a[i]
            if op == "+":
                op = "-"
            else:
                op = "+"
    return ans


print(min(check("+"), check("-")))
