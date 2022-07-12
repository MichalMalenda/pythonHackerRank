s = input()
a=False
b=False
c=False
d=False
e=False
for x in range(len(s)):
    if s[x].isalnum() and a!=True:
        a=True
    if s[x].isalpha() and b!=True:
        b=True
    if s[x].isdigit() and c!=True:
        c=True
    if s[x].islower() and d!=True:
        d=True
    if s[x].isupper() and e!=True:
        e=True
print(a)
print(b)
print(c)
print(d)
print(e)