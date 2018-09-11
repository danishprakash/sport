

def palindrome_number(n):
    # 1 2 3 2 1
    t1, t2 = 0, len(n)
    while t1 < len(n)/2:
        if n[t1] == n[t2]:
            pass
        elif n[t1] != n[t2]:
            return False
        t1 += 1
        t2 -= 1
    return Tr
