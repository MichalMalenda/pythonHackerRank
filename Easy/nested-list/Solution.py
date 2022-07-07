def fsmnin(a):
    splitList = a
    splitList = [float(numeric_string) for numeric_string in splitList]
    z = filter((min(splitList)).__ne__,splitList)
    return min(z)

def nes_lis(pplist):
    temp2 = 0
    out = []
    vals = []
    for x in range(len(pplist)):
        vals.append(float(pplist[x][1]))
    valueMin = fsmnin(vals)
    for y in range(len(pplist)):
        if float(pplist[y][1]) == valueMin:
            out.append(pplist[y][0])
    out.sort()
    for z in range(len(out)):
        print(out[z])

    #print(out)


pplist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    person = [name, score]
    pplist.append(person)
nes_lis(pplist)