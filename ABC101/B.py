N = input()
total = 0
for w in N:
    total += int(w)
if int(N) % total == 0:
    print('Yes')
else:
    print('No')
