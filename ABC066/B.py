s = input()
n = len(s)
for i in range(1, n):
    if (n - i) % 2 == 0:
        if s[0:(n - i) // 2] == s[(n - i) // 2:n - i]:
            print(n - i)
            exit()
