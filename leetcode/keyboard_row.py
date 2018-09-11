def findWords(words):
    l1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    l2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    l3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
   
    k = 0
    temp = [l1, l2, l3]
    res = []

    for i in range(len(words)):
        clear = False
        k = 0
        j = 0
        while j < len(words[i]):
            #print(words[i][j].lower(), i, j, k, len(words[i]))
            if words[i][j].lower() not in temp[k]:
                #print("first if")
                j = 0
                k += 1
                if k > 2:
                    break
            elif j == len(words[i])-1:
                #print("else if")
                res.append(words[i])
                break
            else:
                j += 1
    print(res)

findWords(["Hello", "Alaska", "Dad", "Peace", "Pole", "Pop", "Qwertv", "Bam",
    "kale", "mnm"])
