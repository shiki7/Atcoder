s = input()
if len(set(s)) == len(s) and not s.isupper() and not s.islower():
    print("Yes")
else:
    print("No")
