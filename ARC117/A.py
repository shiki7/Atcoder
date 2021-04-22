A, B = map(int, input().split())
ans = []
total = 0
if A > B:
    for i in range(1, A+1):
        ans.append(i)
        total += i
    for i in range(1, B):
        ans.append(-i)
        total -= i
    ans.append(-total)
elif A < B:
    for i in range(1, B+1):
        ans.append(-i)
        total += i
    for i in range(1, A):
        ans.append(i)
        total -= i
    ans.append(total)
else:
    for i in range(1, A+1):
        ans.append(i)
        ans.append(-i)
print(*ans)
