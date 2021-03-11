T = int(input())
s = []
for _ in range(T):
    s.append(int(input()))
    _ = [int(input()) for _ in range(3)]

for i in range(T):
    print("0" * s[i] + "1"*s[i] + "0")
