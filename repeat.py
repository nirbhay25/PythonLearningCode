a = "NIrbhay"
length = len(a)
flag = 0
for i in range(0,length-1):
    if a[i] == a[i+1]:
        flag = 1
    print(i, end = ' ')
    print(a[i])
print(flag)