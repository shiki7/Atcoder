s = input()
total = int(s[0])

op = ['+', '-']
for i in op:
    for j in op:
        for k in op:
            cmd = s[0] + i + s[1] + j + s[2] + k + s[3]
            if eval(cmd) == 7:
                print(cmd + "=7")
                exit()
