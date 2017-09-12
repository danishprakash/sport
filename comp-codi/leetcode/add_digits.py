# https://leetcode.com/problems/add-digits

def addDigits(num):
    while num//10 > 0:
        num = sum(list(map(int, str(num))))
    return num

print(addDigits(38))
        
