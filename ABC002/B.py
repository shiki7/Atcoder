word = input()
li = ['a', 'i', 'u', 'e', 'o']
ans = ""
for w in word:
    if w not in li:
        ans += w
print(ans)
