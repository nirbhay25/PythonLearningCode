#normal function
def larger(a,b):
    if a > b:
        return a
    else:
        return b
d = larger(45,60)
print(d)

#using lambda function
c = lambda a, b: a if a > b else b
print(c(4,5))
#OR
print((lambda a, b: a if a > b else b)(5,6))

lst = [(12,45), (33,4), (2,5)]
lst.sort()
print(lst)      #[(2, 5), (12, 45), (33, 4)]
def k(x):
    return x[1]
lst.sort(key = k)   
[print(lst)]    #[(33, 4), (2, 5), (12, 45)]