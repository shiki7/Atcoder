n = int(input())
a = list(map(int, input().split()))

total = sum(a)
if total % n != 0:
    print(-1)
    exit()

avr = total // n
ans = 0
for i in range(n-1):
    if a[i] != avr:
        ans += 1
        if a[i] > avr:
            a[i+1] += a[i] - avr
            a[i] = avr
        else:
            a[i+1] -= avr - a[i]
            a[i] = avr
print(ans)
