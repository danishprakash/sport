def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if abs(x) > (2**31)-1:
        return 0

    x = list(str(x))

    if x[0] == '-':
        flag = True
    else:
        flag = False

    if flag is True:
        del x[0]
        res = -(int(''.join(x[::-1])))
        return res if abs(res) < (2**31)-1 else 0
    else:
        res = int(''.join(x[::-1]))
        return res if abs(res) < (2**31)-1 else 0

print(reverse(int(input())))
