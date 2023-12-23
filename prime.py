num = int(input())
flag = 1
for i in range(2,num):
    if num % i == 0:
        flag = 0
if flag == 0:
    print("False")
else:
    print("True")
 