S = input()
tmp = S[0]
for num in S[1:]:
    if num == tmp:
        print('Bad')
        exit()
    tmp = num
print('Good')
