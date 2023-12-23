#APPEND
name = ['Nirbhay', 'Anand', 'Richa','tuktuk']
#append insert the element at the end of the string.
name.append(45)
print(name)
surname = ['Anand','gowda','chaudhary']
#we can also append a list into a list, the appended list will act as a new element inside the list
surname.append(name)
print(surname)

#EXTEND
age = ['18','34','56']
#extend the list but concating the new list after the first list.
name.extend(age)
print(name)