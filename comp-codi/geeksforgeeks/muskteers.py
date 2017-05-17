t = int(input())

for i in range(t):
    n = input()
    temp = 1
    flag = 0
    for j in range(len(n)):
        if n[j] == '0':
            if j==0:
                temp=0
                flag = 1
            elif temp-(j-1) == 0:
                temp = j
                flag = 1
            else:
                flag = 0
                break
    if flag == 1:
        print("YES")
    else:
        print('NO')
