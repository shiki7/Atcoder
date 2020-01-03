s = input()
k = int(input())

if len(s) == 1:
    print(k//2)
    exit()
if s.count(s[0]) == len(s):
    print(len(s)*k//2)
    exit()

count = 0
flag = True
for i in range(1, len(s)):
    if not flag:
        flag = True
        continue
    if s[i] == s[i-1]:
        count += 1
        flag = False

count2 = 0
flag = True
s = s*2
for i in range(1, len(s)):
    if not flag:
        flag = True
        continue
    if s[i] == s[i-1]:
        count2 += 1
        flag = False
# 連結部分の数を加える
print(count * k + (count2-count*2)*(k-1))
