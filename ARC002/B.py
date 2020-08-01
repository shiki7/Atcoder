import datetime

a = datetime.datetime.strptime(input(), '%Y/%m/%d')
while True:
    if a.year % (a.month * a.day) == 0:
        print("{:02d}/{:02d}/{:02d}".format(a.year, a.month, a.day))
        exit()
    a += datetime.timedelta(days=1)
