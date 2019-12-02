# TLE

n = int(input())
s = input()

count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            f1 = False
            f2 = False
            p1 = 0
            p2 = 0
            for i in range(0, n-2):
                if int(s[i]) == a:
                    f1 = True
                    p1 = i
                    break
            if f1:
                for j in range(p1+1, n-1):
                    if int(s[j]) == b:
                        f2 = True
                        p2 = j
                        break
            if f2:
                for k in range(p2+1, n):
                    if int(s[k]) == c:
                        count += 1
                        break
print(count)
