def binaryRep(num):
    l1 = []
    while num >= 1:
        l1.append(str(num%2))
        num = num//2
    l1 = [str(l1[i]) for i in range(len(l1))]
    return l1

def addLeadingZeroes(l1, n):    
    for i in range(len(l1), n):
        l1.append('0')
    return l1

def hamminDistance(x, y):
    a = binaryRep(x)
    b = binaryRep(y)
    count = 0
    if len(a) > len(b):
        b = addLeadingZeroes(b, len(a))
    else: 
        a = addLeadingZeroes(a, len(b))
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

print(hamminDistance(1, 4))
