def isHappy(num):
    temp = 0
    num = [int(x) for x in str(num)]
    #print(len(num))
    while temp != 1:
        temp = 0
        for i in range(len(num)):
            temp += int(num[i])**2
        #print(temp)
        num = [int(x) for x in str(temp)]

isHappy(19)
