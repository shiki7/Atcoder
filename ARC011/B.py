d = dict()
d = {"b": 1, "c": 1, "d": 2, "w": 2, "t": 3, "j": 3, "f": 4, "q": 4, "l": 5,
     "v": 5, "s": 6, "x": 6, "p": 7, "m": 7, "h": 8, "k": 8, "n": 9, "g": 9, "z": 0, "r": 0,
     "a": "", "i": "", "u": "", "e": "", "o": "", "y": "", ",": "", ".": ""}

N = int(input())
S = list(input().split())
ans = []
for i in range(N):
    w = S[i].lower()
    x = ""
    for i in range(len(w)):
        d[w[i]]
        x += str(d[w[i]])
    if x != "":
        ans += [x]
print(*ans)
