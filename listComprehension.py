n = int(input())
list = []
for i in range(0,n):
    element = input()
    list.append(element)
list.sort()
print(list)  
if list[n-1] > list[n-2]:
    print(list[n-2])
else:
    for i in range(n-2, 0):
        if list[i] > list[i-1]:
            print(list[-1])
        else:
            print(-1)
