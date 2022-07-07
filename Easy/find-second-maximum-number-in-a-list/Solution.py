def fsmnial(n,a):
    splitList = a.split(" ")
    splitList = [int(numeric_string) for numeric_string in splitList]
    z = filter((max(splitList)).__ne__,splitList)
    print(max(z))
    #for x in reversed(range(n)):


n = int(input())
a = input()
fsmnial(n, a)