name = input()
length = len(name)
flag = 0
for i in range(length):
    if name[i] == name[length-1-i]:
        flag = 0
    else:
        flag = 1
if flag == 1:
    print("Not Pallindrome")
else:
    print("Pallindrome")
   