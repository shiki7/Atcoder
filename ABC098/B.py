N = int(input())
S = input()
s_list = [s for s in S]
max_count = 0
for i in range(1, N):
    max_count = max(max_count, len(set(s_list[:i]) & set(s_list[i:])))
print(max_count)
