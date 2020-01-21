n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
mod = 10**9+7
for i in range(0, n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            cnt1 += 1
        elif a[i] < a[j]:
            cnt2 += 1
print(((k*(k+1)//2 % mod) * cnt1 % mod + ((k-1)*k//2 % mod)*cnt2 % mod) % mod)
