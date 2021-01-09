S = input()
a = 0
b = 0
for i in range(5):
    if S[i] == "o":
        a += 1
        b = 0
    else:
        b += 1
        a = 0
    if a >= 3:
        print("o")
        exit()
    if b >= 3:
        print("x")
        exit()
print("draw")
