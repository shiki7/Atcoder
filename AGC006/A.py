n = int(input())
s = input()
t = input()

match_count = 0
for i in range(n):
    if s[i:] == t[:n-i]:
        match_count = n-i
        break
print(2*n - match_count)
