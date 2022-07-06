from itertools import product
kNum, mNum = map(int,input().split())
def squareN(n):
    return int(n)**2
numList = []
for i in range(kNum):
    numList.append(map(squareN,input().split()[1:]))
Max=0
for T in product(*numList):
    Sum=sum(T)%mNum
    if Sum>Max:
        Max=Sum
print(Max)