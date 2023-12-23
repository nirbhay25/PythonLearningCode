#global variable
a = 5
def func():
    print(a)
func()

#local varaible
def func2():
    x =3 #local varaible
    print(x)
func2()
#print(x)  #this will throw an error as the 'x' variable 
          #gets deleted as soon as the func2() gets executed

#global fn
a = 5
def func():
    print(a)
func()

def intro(name, age, hobby):
    return name, age, hobby
a, b, c = intro("Nirbhay", 25, "Coding")
print(a, b, c)  #here we used unpacking
d = intro("Nirbhay", 25, "Coding")
print(d)   
print(type(d))
func()