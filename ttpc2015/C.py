S = input()

for n in range(100, 2, -1):
    tmp = "o" * n + "kayama"
    if n % 3 == 0:
        a = "Ookayama"
    elif n % 3 == 1:
        a = "okayama"
    else:
        a = "Okayama"
    S = S.replace(tmp, a)

print(S)
