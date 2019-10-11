s = input()

op_count = len(s) - 1
op_list = []
for i in range(2**op_count):
    op = [''] * op_count
    for j in range(op_count):
        if (i >> j) & 1:
            op[op_count - 1 - j] = '+'
    op_list.append(op)

ans = 0
for i in range(2**op_count):
    cur = 1
    t = s
    for j in range(op_count):
        if op_list[i][j] == '+':
            t = t[:j + cur] + "+" + t[j + cur:]
            cur += 1
    ans += eval(t)
print(ans)
