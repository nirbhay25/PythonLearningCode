n = 'Nirbhay Anand'
print(n[0])
print(n[-1])
size = len(n)
print(size)
print(n[-size])
#positive indexing starts with 0,1,2,3....n-1
#negative indexing starts with -1,-2,-2,....[-length]  

#slicing the string
print(n[0:3])
print(n[0:size])
print(n[0:4])
print(n[:])# this will give you the whole list
print(n[::  ])
print(n[-1:-size])
print(n.capitalize())

n = 'nirbhay anand'
print(n.capitalize()) #Nirbhay anand
print(n.title())  #Nirbhay Anand
print(n.upper()) #NIRBHAY ANAND
print(n.lower()) #nirbhay anand
print(n.find("ay")) #5
print(n.count("n")) #3
print(n.replace("a","A")) #nirbhAy AnAnd

#split 
print(n.split()) #['nirbhay', 'anand']
print(n.split("a")) #['nirbh', 'y ', 'n', 'nd']

n = 'Nirbhay'
age = '25'
size = '2XL'
print(n.isalpha()) #true
print(n.islower()) #false
print(n.isupper()) #false
print(n.isnumeric()) #false
print(age.isnumeric()) #true
print(size.isnumeric()) #false


#Srring Operations
firstName = input()
lastName = input()
age = input()
print("My name is {} {} and my age is {}".format(firstName, lastName, age))
print(" {} {} and age {}".format(firstName,lastName,age))
a = input()
b = input()
print(a + b)
print(a + " " +b)