cnt = int(input())
S = input()
if cnt == 0:
    print('Yes')
    exit()
for i in range(len(S)):
    if S[i] == "+":
        cnt += 1
    else:
        cnt -= 1
    if cnt == 0:
        print('Yes')
        exit()
print('No')
