x1, v1, x2, v2 = [int(s) for s in input().split()]
gap = abs(x1-x2)

while(True):
    x1 += v1
    x2 += v2
    pregap = gap
    gap = abs(x1 - x2)
    if gap == 0:
        print("YES")
        break
    elif gap >= pregap or (x1 <= x2 and v1 < v2):
            print("NO")
            break
