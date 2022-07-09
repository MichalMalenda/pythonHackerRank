def decisionControl(commandList):
    out = []
    for y in range(len(commandList)):
        if (commandList[y]).startswith('insert'):
            vals = commandList[y].split(" ")
            out.insert(int(vals[1]),int(vals[2]))
        elif (commandList[y]).startswith('print'):
            print(out)
        elif (commandList[y]).startswith('remove'):
            vals = commandList[y].split(" ")
            out.remove(int(vals[1]))
        elif (commandList[y]).startswith('append'):
            vals = commandList[y].split(" ")
            out.append(int(vals[len(vals)-1]))
        elif (commandList[y]).startswith('sort'):
            out.sort()
        elif (commandList[y]).startswith('pop'):
            out.pop(len(out)-1)
        elif (commandList[y]).startswith('reverse'):
            out.reverse()

n = int(input())
commandList = []
for x in range(n):
    commandList.append(input())
decisionControl(commandList)