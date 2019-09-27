n = int(input())
s = [int(input()) for _ in range(n)]

total = sum(s)
s.sort()
if total % 10 != 0:
    print(total)
else:
    for i in range(n):
        if (total - s[i]) % 10 != 0:
            print(total - s[i])
            exit()
    print(0)
