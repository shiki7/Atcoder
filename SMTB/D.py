n = int(input())
s = input()

# TLE
count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            flag = 0
            for i in range(0, n-2):
                if flag == 1:
                    break
                if int(s[i]) == c:
                    for j in range(i+1, n-1):
                        if flag == 1:
                            break
                        if int(s[j]) == b:
                            for k in range(j+1, n):
                                if int(s[k]) == a:
                                    count += 1
                                    flag = 1
                                    break
print(count)
