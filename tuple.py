t = (2)
t2 = (2,)
print(type(t))
print(type(t2))

#tuples areen't mutable but if the elements inside tuples are list. We can mutate the list.
t3 = ([4,5,6,3],45,[3,4,9])
t3[0]
t3[0][2] = 'NIRBHAY' 
t3[2][2] = 'ANAND'
print(t3)
print()
#unpacking a tuple
t = (2, 5 , 'Nirbhay', True)
a, b, c, d = t
print(t)
print(a, b, c, d)
print()

#TUPLE OPERATIONS
t2 = (2, 5 , 'Nirbhay', True, 'Anand', 23, 44)
t2.count('Nirbhay')
t2.index(True)
len(t)
# tuples are iterable
for i in t:
    print(i)
#concatanation (+,*)
t5 = t + t2
print(t5)
#we can change tuple into lists
t5 = list(t5)
print(t5)

N = input()
new_list = list(N)
print(new_list)