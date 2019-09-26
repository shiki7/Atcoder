n = int(input())
a = list(map(int, input().split()))

score_list = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
counter = [0] * 9
for i in range(len(a)):
    if a[i] >= 3200:
        counter[8] += 1
    for j in range(8):
        if a[i] < score_list[j]:
            counter[j] += 1
            break
ans_min = 0
for i in range(len(counter) - 1):
    if counter[i] != 0:
        ans_min += 1
if counter[8] >= 1:
    ans_max = ans_min + counter[8]
    if ans_min == 0:
        ans_min += 1
else:
    ans_max = ans_min
print(ans_min, ans_max)
