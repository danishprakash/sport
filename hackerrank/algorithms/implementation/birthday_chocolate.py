n = int(input())
s = [int(x) for x in input().split()]
d, m = [int(x) for x in input().split()]
count = 0
 
for i in range(n-m+1):
    sum_ = sum(s[i:i+m])
    if sum_ == d:
        count += 1

print(count)
