def pyifelse(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n < 0:
        print("Weird")
    else:
        print("Not Weird")

n = int(input())
pyifelse(n)