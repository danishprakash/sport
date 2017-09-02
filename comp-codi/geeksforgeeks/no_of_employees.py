d = dict()
man = dict()
nman = dict()
n = int(input())
for i in range(n):
    a, b = input().split()
    d[a] = b
for key in d.keys():
    man[key] = 0
for key in d.keys():
    for value in d.values():
        if key == value:
            man[key] += 1

for key in man.keys():
    if man[key] != 0:
        nman[key] = man[key]
print(nman)

for key in nman.keys():
    nman[key] += nman[key]

#for key in man.keys():
#    for value in d.values():
#        if key == value:
#            print(key, value)
#            man[key] += man[d[value]]
print(man)
