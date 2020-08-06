N = int(input())
a = list(map(int, input().split()))
ans = -float('inf')
for i in range(N):
    ta = -float('inf')
    ao = -float('inf')
    for j in range(N):
        if i == j:
            continue
        elif i < j:
            tmp = sum(a[i+1:j+1:2])
            if tmp > ao:
                ta = sum(a[i:j+1:2])
                ao = tmp
        else:
            tmp = sum(a[j+1:i+1:2])
            if tmp > ao:
                ta = sum(a[j:i+1:2])
                ao = tmp
    ans = max(ta, ans)
print(ans)
