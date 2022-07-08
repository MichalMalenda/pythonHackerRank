n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
tocalc = student_marks[query_name]
temp=0
for x in range(len(tocalc)):
    temp+=float(tocalc[x])
temp = "{:.2f}".format(temp/len(tocalc))
print(temp)