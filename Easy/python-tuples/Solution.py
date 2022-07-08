n = int(input())
integer_list = map(int, input().split())
tuple = ()
for x in integer_list:
    tuple+=(x,)
print(hash(tuple))