def print_formatted(number):
    width = len("{0:b}".format(number))
    for x in range(number):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(x+1, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)