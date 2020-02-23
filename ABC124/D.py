n, k = map(int, input().split())
s = input()
b = [1]
if s[0] == "0":
    b = [0, 1]
for i in range(1, n):
    if s[i-1] != s[i]:
        b += [1]
    else:
        b[-1] += 1
if s[-1] == "0":
    b += [0]
if len(b)//2 <= k:
    print(n)
    exit()

x = a = sum(b[:k*2+1])
for i in range(k, len(b)//2):
    a += b[i*2+1]+b[(i+1)*2]
    a -= b[(i-k)*2]+b[(i-k)*2+1]
    x = max(a, x)
print(x)
