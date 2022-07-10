import re
first_multiple_input = input().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
out=''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for x in range(m):
    for y in range(n):
        out+=matrix[y][x]
    #out+=' '
#print(out)    
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
out = re.sub(pattern,r'\1 ', out)
print(out)