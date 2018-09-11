# http://practice.geeksforgeeks.org/problems/find-the-fine/0

t = int(input())

def calculateFine(cars, fine, isEven, n):
    res = []
    for k in range(n):
        if not(cars[k] % 2 == 0 ^ isEven):
            continue
        else:
            res.append(fine[k])
    return sum(res)

for i in range(t):
    n, date = map(int, input().split())
    cars = list(map(int, input().split()))
    fine = list(map(int, input().split()))
    isEven = True if date % 2 == 0 else False
    print(calculateFine(cars, fine, isEven, n))
