def binaryRep(num):
    l1 = []
    while num >= 1:
        l1.append(str(num%2))
        num = num//2
    l1 = [str(l1[i]) for i in range(len(l1))]
    l1 = l1[::-1]
    return l1

def decimalRep(l1):
    temp = len(l1)-1
    for i in range(len(l1)):
        l1[i] = int(l1[i]) * (2**temp)
        temp -= 1
    return (sum(l1))

def findComplement(num):
    l1 = binaryRep(num)
    for i in range(len(l1)):
        if l1[i] == '0':
            l1[i] = '1'
        elif l1[i] == '1':
            l1[i] = '0'
    return decimalRep(l1)

print(findComplement(int(input())))
