s = input()
a = list(map(int, input().split()))
cur = 0
for i in range(len(a)):
    s = s[:a[i]+cur] + '"' + s[a[i]+cur:]
    cur += 1
print(s)
