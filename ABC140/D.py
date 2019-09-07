# not clear
N, K = map(int, input().split())
S = input()

max_total = 0
total = 0

for l in range(0, N-1):
    if (S[l] == 'R'):
        if l == 0:
            T1 = 'L' + S[1:]
        else:
            T1 = S[:l-1] + 'L' + S[l:]
    else:
        if l == 0:
            T1 = 'R' + S[1:]
        else:
            T1 = S[:l-1] + 'R' + S[l:]
    for r in range(l+1, N):
        if (T1[r] == 'R'):
            T2 = T1[:r-1] + 'L' + T1[r:]
        else:
            T2 = T1[:r-1] + 'R' + T1[r:]
        if l == 0:
            tmp = T2[r]
            T2 = T2[l] + T2[r:]
            T2 = tmp + T2[l:]
        else:
            tmp = T2[r]
            T2 = T2[:r-1] + T2[l] + T2[r:]
            T2 = T2[:l-1] + tmp + T2[l:]
        for i in range(N-1):
            if T2[i] == T2[i+1]:
                total += 1
        print(T2)
        print(total)
        max_total = max(max_total, total)
        total = 0
print(max_total)
