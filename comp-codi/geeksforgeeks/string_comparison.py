t = int(input())

for i in range(t):
    l1 = input()
    l1 = l1.split(" ")
    if l1 == None or i%2 == 0:
        continue
    print(l1)
    j = 0
    while True:
        if l1[0][j] != l1[1][j] or l1[0][j] == 'n' or l1[1][j] == 'n':
            #print(l1[0][j:j+2], l1[1][j])
            if l1[0][j:j+2] == 'ng' and (l1[1][j] >= 'o'):
                print(-1)
                break
            else:
                print(1)
                break

            if l1[1][j:j+2] == 'ng' and (l1[0][j] >= 'o'):
                print(1)
                break
            else:
                print(-1)
                break

            if l1[0][j] > l1[1][j]:
                print(1)
                break
            elif l1[0][j] < l1[1][j]:
                #print(l1[0][j], l1[1][j])
                print(-1)
                break
        elif l1[0] == l1[1]:
            print(0)
            break
        j += 1
