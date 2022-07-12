from itertools import permutations
s=input().split(' ')
b=list(permutations(s[0],int(s[1])))
b.sort()
for x in range(len(b)):
    print("".join(b[x]))