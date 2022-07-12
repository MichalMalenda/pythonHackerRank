#this should work but for some reason tasks fail anyway
#from itertools import combinations
#s=input().split(' ')
#b=[]
#for y in range(int(s[1])):
#    a=list(combinations(s[0],y+1))
#    a.sort()
#    b+=a
#for x in range(len(b)):
#    print("".join(b[x]))
from itertools import combinations
a,b = input().split()
print(*[''.join(j) for i in range(1,int(b)+1) for j in combinations(sorted(a),i)],sep='\n')