t = int(input())

for i in range(t):
    a, b = input().split()
    #print(type(a), b)
    n = 0
    if len(a) > len(b):
        n = len(a)
    else:
        n = len(b)
    j = -1
    count = 0
    carry = 0
    for i in range(n):
        #print(j)
        if j >= abs(len(a)):
        if j == -1:
            #print("here")
            if int(a[j:]) + int(b[j:]) + carry >= 10:
                carry = 1
                count += 1
        elif int(a[j:j+1]) + int(b[j:j+1]) + carry >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
        j -= 1
    print(count)
