N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')
sum_rgb = r*g*b

# rgbの組み合わせの総数から距離が等しいものを引く
for i in range(N-2):
    for j in range(i+1, N-1):
        k = j + (j-i)
        if k > N-1:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            sum_rgb -= 1
print(sum_rgb)
