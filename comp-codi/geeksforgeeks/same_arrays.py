def sortarr(a):
    for i in range(len(a)):


        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swap(a[j], a[j+1])

def swap(x, y):


    y = x+y
    x = y-x
    y = y-x
    print(x,y)

# a1 = [int(x) for x in input().split()]
# a2 = [int(x) for x in input().split()]
x=2
y=8

print(x,y)
swap(x,y)
# print(x,y)
