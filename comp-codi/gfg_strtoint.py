def atoi(string):
    for i in range(len(string)):
        if string[i].isalpha():
            return -1
        elif string[i] in ['-']:
            for j in range(i+1,len(string)):
                if not(string[j].isdigit()):
                    return -1
            return int(string[i])
        elif string[i].isdigit():
            for k in range(0, len(string)):
                if not(string[k].isdigit()):
                    return -1
            return int(string)

n = int(input())
for i in range(n):
    print(atoi(input()))
