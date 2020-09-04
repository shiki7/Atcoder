s = input()
i = 0
s = s[::-1]
for i in range(len(s)):
    if s[i:i+2] == "AW":
        s = s[:i] + "CA" + s[i+2:]
print(s[::-1])
