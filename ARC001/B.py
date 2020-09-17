a, b = map(int, input().split())
diff = abs(b - a)
ans = 0
ans += diff // 10
diff = diff % 10
if diff == 4 or diff == 9:
    ans += 2
elif diff == 5:
    ans += 1
elif diff == 1 or diff == 2 or diff == 3:
    ans += diff
elif diff == 6 or diff == 7:
    ans += 1 + (diff % 5)
elif diff == 8:
    ans += 3
print(ans)
