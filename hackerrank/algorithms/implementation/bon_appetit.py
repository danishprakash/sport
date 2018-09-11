n, k = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
amt = int(input())

if amt > ((sum(f)-f[k])/2):
    print(f[k]//2)
else:
    print('Bon Appetit')
