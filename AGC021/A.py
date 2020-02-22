s = input()
digit = len(s)

first_num = int(s[0])
a = 0
a = 9*(digit-1) + int(s[0]) - 1

b = 0
for i in s:
    b += int(i)
print(max(a, b))
