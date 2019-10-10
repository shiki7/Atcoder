s = input()
a = 'WBWBWWBWBWBW' * 2
ans_list = [
    'Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si'
]
for i in range(12):
    if s[:12] == a[i:i + 12]:
        print(ans_list[i])
        exit()
