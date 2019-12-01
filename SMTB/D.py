n = int(input())
s = input()

# どこか間違ってる
count = 0
for a in range(9):
    for b in range(9):
        for c in range(9):
            flag = 0
            for i in range(0, n-2):
                if flag == 1:
                    break
                if int(s[i]) == b:
                    for j in range(i+1, n-1):
                        if flag == 1:
                            break
                        if int(s[j]) == a:
                            for k in range(j+1, n):
                                if int(s[k]) == c:
                                    count += 1
                                    flag = 1
                                    break
print(count)
