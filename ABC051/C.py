sx, sy, tx, ty = map(int, input().split())

mv_x = tx - sx
mv_y = ty - sy

ans = ''
ans += 'R' * mv_x + 'U' * mv_y
ans += 'L' * mv_x + 'D' * mv_y
ans += 'D' + 'R' * (mv_x+1) + 'U' * (mv_y+1) + 'L'
ans += 'U' + 'L' * (mv_x+1) + 'D' * (mv_y + 1) + 'R'

print(ans)
