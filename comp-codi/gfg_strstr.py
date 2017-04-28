def strstr(str, substr):
    index = -1
    for i in range(len(str)):
        if str[i:i+len(substr)] == substr:
            index = i
            break
    return index


if __name__=='__main__':
    n = int(input())
    for i in range(n):
        str,substr = input().strip().split()
        print(strstr(str, substr))
