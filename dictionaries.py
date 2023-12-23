d = {}
print(type(d))
print(d)
fruits = {
    "Apple" : 120,
    "mango" : 30,
    "pinapple" : 40
}
print(fruits)

#zip(key,values)
name = ["Nirbhay","Nirlep","Sudiksha", "Daraksha"]
age = [25, 26, 18, 21]
ages  = dict(zip(name, age))
print(ages)
print(ages["Nirbhay"]) # we can access the values of the dictionaries by using key.

#print(ages["Pritika"])   #this will throw an error so to avoid this we will use .get functions

print(ages.get("Sudiksha")) 
print(ages.get("Pritika", "Not Available"))