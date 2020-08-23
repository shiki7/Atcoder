a, b, t = map(int, input().split())
d = b-a

for i in range(3000):
    if b + d * i >= t:
        print(b + d*i)
        exit()
