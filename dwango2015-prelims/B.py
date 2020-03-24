S = input()


def calc(x):
    return x*(x+1)//2


S += '00'
cnt = 0
skip_flag = False
ans = 0
for i in range(len(S)+1):
    if skip_flag:
        skip_flag = False
        continue
    if S[i:i+2] == '25':
        cnt += 1
        skip_flag = True
    else:
        ans += calc(cnt)
        cnt = 0
print(ans)
