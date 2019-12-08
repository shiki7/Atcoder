s = input()
a = s[::-1]
count = 0
for i in range(len(s)):
    if a[i] != s[i]:
        count += 1
print(count//2)
