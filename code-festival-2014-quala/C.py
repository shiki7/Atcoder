def countLeapYear(x):
    return x//4 - x // 100 + x//400


a, b = map(int, input().split())
print(countLeapYear(b) - countLeapYear(a-1))
