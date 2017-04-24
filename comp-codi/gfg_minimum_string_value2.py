def minimize(s, k, count):
    for char in s:
        count.setdefault(char, 0)
        count[char] += 1
    for i in range(len(count)):
        maxkey = max(count, key=count.get)
        maxval = count[maxkey]
        if k>0:
            count[maxkey] -= (maxval-1)
            k -= (maxval-1)
    return (sum(l*l for l in count.values()))

t = int(input())

for j in range(t):
    s = input()
    k = int(input())
    c = dict()
    if k >= len(s):
        print('0')
        continue
    print(minimize(s,k,c))
