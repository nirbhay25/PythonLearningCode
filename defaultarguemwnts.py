def intro(name, hobby = 'coding'):  #here coding is the default arguement
    print('My name is: ', name)
    print('My hobby is: ', hobby)
print(intro('Nirbhay'))
print(intro('Nirbhay','Singing'))

#NOTE: the default agruement should always be adssigned after a non-default agruement

#arbitrary arguements: when we are passing more than one aggrements but we dont know ow many we will need
def test(*args):
    print(type(args))
    for i in args:
        print(i*i, end= " ")
c = test(2,4,4,6)
print(c)

#keyword agruements: when we are passing key and values as arguements
def intro2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, values in kwargs.items():
        print(key, values)

intro2(name= "Rahul", age = 25)

def mix(a, b, c, age = 23, *args, **kwargs):
    print(a,b,c)
    print(age)
    print(*args)
    print(**kwargs)

print(mix(2,4,5)) #if we do not use args and kwargs it will not show error as minimum req, are the single arguements only
