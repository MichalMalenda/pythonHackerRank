def maximizeIt(k):
    splitList = k.split(" ")
    setsVal = splitList[0]
    moduleVal = splitList[1]
    list = []
    temp2= 0
    out = []
    for x in range(int(setsVal)):
        templist = []
        a = input()
        templist.append(a)
        list.append(templist)
    for y in range(int(setsVal)):
        splitList2 = list[y]
        #print(splitList2)
        for z in range(int(len(splitList2))):
            splitList3 = splitList2[z]
            #print(splitList3.split())
            splitList3 = splitList3.split()
            #print(splitList3)
            for m in range(int(len(splitList3))):
                #if splitList3[m] != " ":
                temp1 = splitList3[m]
                    #print(temp1)
                if int(temp1) > int(temp2):
                    temp2 = temp1
            out.append(temp2)
    #print(out)
    result = 0
    for n in range(len(out)):
        result += int(out[n]) * int(out[n])
    result = result % int(moduleVal)
    print(result)

k = input()
maximizeIt(k)