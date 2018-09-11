#http://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1

def convertFive(number):
    number = str(number)
    for i in range(len(number)):
        if number[i] == '0':
            number = (number[0:i] + '5' + number[i+1:])
    return int(number)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
