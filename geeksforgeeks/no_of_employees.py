# http://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/

d = dict()
man = dict()
n = int(input())

''' Initializing the d dict with user input and initializing a new dictionary
man with values 0 for every key in d 
'''
for i in range(n):
    a, b = input().split()
    d[a] = b
    man[a] = 0

''' Checking each key in dict d with all the values in dict d and incrementing
man[key] count
line 22 checks if the manager is an employee of itself and if yes, then
decrement
'''
for key, lvalue in d.items():
    for value in d.values():
        if key == value:
            man[key] += 1
    if key == lvalue:
        man[key] -= 1

''' Finally traversing all the items in dict d and see if they are present in
dict man i.e see if they are managers. If yes, check if they are managing each
other and hence update their respective count
'''
for key, value in d.items():
    if key in man.keys() and value in man.keys() and key != value:
        man[value] += man[key]

print(man)

