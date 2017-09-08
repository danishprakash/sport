# https://leetcode.com/problems/add-binary

def binaryRep(num):
    if num == 0:
        return 0
    l1 = []
    while num >= 1:
        l1.append(str(num%2))
        num = num//2
    l1 = [str(l1[i]) for i in range(len(l1))]
    return ''.join(l1[::-1])

def decimalRepresentation(strr):
    strr = strr[::-1]
    num = 0
    for i in range(len(strr)):
        num += (2**i)*int(strr[i])
    return num

def addBinary(a, b):
    return binaryRep(decimalRepresentation(a)+decimalRepresentation(b))

print(addBinary('11', '1'))


