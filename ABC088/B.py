n = int(input())
card = list(map(int, input().split()))
card = sorted(card, reverse=True)
a = 0
b = 0
for i in range(len(card)):
    if i % 2 == 0:
        a += card[i]
    else:
        b += card[i]
print(a - b)
