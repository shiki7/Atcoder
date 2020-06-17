S = list(input().split())
N = int(input())
T = [input() for _ in range(N)]
ans = []


def check(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] != '*' and s2[i] != '*':
            return False
    return True


for i in range(len(S)):
    flag = True
    for j in range(N):
        if check(S[i], T[j]):
            ans.append("*" * len(T[j]))
            flag = False
            break
    if flag:
        ans.append(S[i])
print(*ans)
