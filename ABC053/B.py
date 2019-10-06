s = input()

a = 0
b = 0
for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break
for i in range(1, len(s)):
    if s[-i] == 'Z':
        b = len(s) - i
        break
print(b-a+1)
