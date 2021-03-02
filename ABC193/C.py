N = int(input())
s = set()

for i in range(2, int(N**0.5) + 1):
    x = i**2
    while x <= N:
        s.add(x)
        x *= i
print(N - len(s))
