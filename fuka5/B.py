import datetime

while True:
    datetime_str = input()
    if datetime_str == '0':
        exit()
    year = int(datetime_str.split('/')[0])
    y_cnt = 0
    while year > 2000:
        year -= 400
        y_cnt += 400
    s = str(year) + '/' + datetime_str[datetime_str.index('/') + 1:]
    t = datetime.datetime.strptime(s, '%Y/%m/%d %H:%M:%S')

    dt = int(input(), 2)
    dd, ds = divmod(dt, 86400)
    t += datetime.timedelta(days=dd, seconds=ds)
    y = t.year + y_cnt
    print(str(y) + '/' + t.strftime('%m/%d %H:%M:%S'))
