def merge_the_tools(string, k):
    splitList = list(string)
    printSet=[]
    temp = []
    for x in range(len(splitList)):
        temp.append(splitList[x])
        if (x+1) % k ==0:
            #print(temp)
            printSet.append(list(dict.fromkeys(temp)))
            temp = []
    #print(printSet)
    for row in printSet:
        print("".join(map(str, row)))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)