n = int(input())
p = {}
for x in range(n):
    new_key = input()
    new_age = int(input())
    p[new_key] = new_age
print(p)
count = 0
for i in p:
    count = count + p[i]
print(count)
    



