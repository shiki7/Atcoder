S = input()
ACGT = ['A', 'C', 'G', 'T']
count = 0
max_count = 0
for w in S:
    if w in ACGT:
        count += 1
    if count > max_count:
        max_count = count
    if w not in ACGT:
        count = 0
print(max_count)
