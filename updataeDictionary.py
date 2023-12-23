fruits = {
    "Apple" : 120,
    "mango" : 30,
    "pinapple" : 40
}
#by changing the key
fruits["banana"] = {"small": 90, "large": 120}
print(fruits) 
fruits["mango"] = 32
print(fruits)   

#update the dictionary
new = {"grapes": 120, "oranges" : 40, "cherry": 21}
fruits.update(new)
print()
print('After updating the new values: ')
print(fruits)

#deleting data from dictionary
#pop
print(fruits)
fruits.pop("banana")
print(fruits)
fruits.popitem()#this will delete the last item in the dictionary
print(fruits)
del fruits #this will delete the fruits dictionary only
#print(fruits)
print()

#iterating in the dictionary
fruits1 = {
    "Apple" : 120,
    "mango" : 30,
    "pinapple" : 40,
    "cherry" : {"apple": 40, "banana" : 60}
}
print(fruits1)
for i in fruits1:
    print(i)
print()
for i in fruits1:
    print(fruits1[i])
print()
for i in fruits1:
    print(i,":",fruits1[i])

 #using item keyword and other keywords as well  
print()
for key, value in fruits1.items():
    print(key, value)
print()
print(fruits1.keys())
print(fruits1.values())
print(fruits1.items())

