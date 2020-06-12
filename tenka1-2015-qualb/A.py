a = []
a.append(100)
a.append(100)
a.append(200)
for i in range(17):
    a.append(a[i]+a[i+1]+a[i+2])
print(a[19])
