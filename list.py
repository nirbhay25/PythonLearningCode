#Insert in List
name = ['Nirbhay', 'Anand', 'Richa','tuktuk']
name.insert(3, 'Pritika')
print(name)
name.remove('Anand')
print(name)

#heterogenous_List
l = [23, 'Nirbhay', True, 1.34]
for i in l:
    print(i, end= ' ')
    print(type(i))

new_list = ['Nirbhay','Anand','is','a','good','boy']
print(new_list)
print()
for i in new_list:
    print(i)
print(new_list[::-1])
print(new_list[0:3])
print(new_list[0:len(new_list)])

#Operation_2
A = []
N = int(input())
for i in range(0,N):
    element = input()
    A.append(element)
X = int(input())
drop_item = A[X]
A.remove(drop_item)
print(A)

#operation_3
name = ['Nirbhay','Pritu','Ravenous']
name.index('Nirbhay')
#print(name.index('Nirbhay'))
name.pop()
print(name)
name.remove('Nirbhay')
print(name)
name = ['Nirbhay','Pritu','Ravenous']
budget = [10, 29, 49 , 544.33, 43, 78]
name.sort()
budget.sort()
print(name)
print(budget)

#list operation
list = [100,200,300,400,100]
print(list)
print(list.count(100))


#print a new list from the original lost having unique values
def unique(li):
    new = []
    for i in li:
        if i not in new:
            new.append(i)
    return new

c = unique([2,4,3,22,2,3,7,6,22,3,4,6])
print(c)
