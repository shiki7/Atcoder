from collections import defaultdict

n = int(input())
b = [int(input()) for _ in range(n-1)]

sub_list = defaultdict(list)
salary_list = defaultdict(lambda: 1)

# 部下リストの生成
for i in range(n-1):
    sub_list[b[i]-1] += [i+1]

for i in reversed(range(n-1)):
    if len(sub_list[i]) == 1:
        salary_list[i] = 2 * salary_list[sub_list[i][0]] + 1
    elif len(sub_list[i]) > 1:
        # 部下が複数の場合に、部下の給与一覧を生成してから、計算する
        sub_salary_list = []
        for j in sub_list[i]:
            sub_salary_list.append(salary_list[j])
        salary_list[i] = max(sub_salary_list) + min(sub_salary_list) + 1
print(salary_list[0])
