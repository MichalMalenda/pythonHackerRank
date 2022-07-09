from collections import OrderedDict
wordList = OrderedDict()
for i in range(int(input())):
    temp = input().strip()
    wordList[temp] = wordList.get(temp, 0) + 1
print (len(wordList))
print (*wordList.values())

#other solution which had Time Limit Exceeded upon running it
#n = int(input())
#wordList = []
#for x in range(n):
#    wordList.append(input())
#count = []
#outList = []
#for y in range(len(wordList)):
#    if wordList[y] not in outList:
#        outList.append(wordList[y])
#for z in range(len(outList)):
#    count.append(wordList.count(outList[z]))
#print(len(outList))
#for i in range(len(count)):
#    print(count[i], end=" ")