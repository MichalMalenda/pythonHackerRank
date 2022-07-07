def listComp(x,y,z,n):
    #newlist = [a for a in range(x)]
    out=[]
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c != n:
                    temp = [a, b, c]
                    out.append(temp)
    print(out)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
listComp(x,y,z,n)