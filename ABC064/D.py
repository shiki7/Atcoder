n = int(input())
s = input()
t = s
counter = 0  # 左:+1 右:-1 最終的に0にしたい
# "("の手前の"）"のインデックスでcounterが負の場合にその数ぶん左に"("を足す
# 最終的にcounterが0でない場合、その数ぶんを左右どちらかに足す

before = ""
i = 0
while i < n:
    if s[i] == "(":
        if i > 0 and before == ")":
            if counter < 0:
                t = "(" * (-counter) + t
                counter = 0
        counter += 1
        before = "("
    else:
        counter -= 1
        before = ")"
    i += 1
if counter > 0:
    t += ")" * (counter)
elif counter < 0:
    t = "(" * (-counter) + t
print(t)
