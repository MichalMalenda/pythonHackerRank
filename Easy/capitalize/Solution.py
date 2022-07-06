def solve(s):
    splitList = s.split(" ")
    for x in range(len(splitList)):
        splitList[x] = str(splitList[x]).capitalize()
    return(' '.join(splitList))