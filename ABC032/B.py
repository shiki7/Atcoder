s = input()
n = int(input())
ans = set()
for i in range(len(s)-n+1):
    ans.add(s[i:i+n])
print(len(ans))
