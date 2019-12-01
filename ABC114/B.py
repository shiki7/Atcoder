s = input()

ans = float('inf')
for i in range(len(s)-2):
    ans = min(abs(753 - int(s[i:i+3])), ans)
    if ans == 0:
        print(0)
        exit()
print(ans)
