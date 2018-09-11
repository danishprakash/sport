n = int(input())

for i in range(n):
    item = temp = int(input())
    while True:
        temp += 1
        if temp%5 == 0:
            if temp-item < 3 and temp >= 40:
                print(temp)
                break
            else:
                print(item)
                break
