n = int(input())

alphabets = [chr(i) for i in range(ord('a'), ord('a') + 26)]

ans = ''
while n > 0:
    n -= 1
    ans = alphabets[n % 26] + ans
    n = n // 26

print(ans)
