import re
S = input()
S = re.sub(r"\s+", " ", S)
print(S.replace(" ", ","))
